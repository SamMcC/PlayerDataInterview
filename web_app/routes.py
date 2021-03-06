"""
Defines routes for the WSGI application
"""
from datetime import datetime

from flask import Flask, render_template, request
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import MultipleResultsFound

from db.user_info import UserInfo
from db.run_info import RunInfo
from db.database import Database
from maths.leger_kcal_calculator import calculate_kcal
from util.logger import get_logger

app = Flask(__name__, template_folder='./templates')
logger = get_logger(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Default path for web application
    """
    if request.method == 'POST':
        return post_index()
    return get_index()


@app.route('/add-run', methods=['GET', 'POST'])
def add_data():
    """
    Path through which users post new run data
    """
    if request.method != 'POST':
        return render_template('add_run.html', page_title='Add Run | kCalTracker')
    # Store data in DB, reload saved data and parse inputs
    date = datetime.fromisoformat(request.form.get('date'))
    time = float(request.form.get('time'))
    distance = float(request.form.get('distance'))
    if date is None or time is None or time < 0 or distance is None or distance < 0:
        logger.debug('User-input issue on POST to add-run. Returning error message.')
        return render_template(
            'add_run.html',
            err='Invalid Inputs, ensure that date is set, and time and distance are greater than 0',
            page_title='Add Run | kCalTracker'
        )
    db = Database()
    session = db.get_session()
    try:
        user = session.query(UserInfo).one_or_none()
        run_info = RunInfo(time_h=time, distance_km=distance, user_id=user.id, date=date)
        session.add(run_info)
        session.commit()
        return my_runs()
    except InvalidRequestError as err:
        logger.debug('Error in adding RunInfo to database.')
        logger.debug('distance: %s, time: %s, date: %s', (distance, time, date))
        session.rollback()
        return render_template(
            'add_run.html',
            err='Failed to add run to database, please check your inputs',
            page_title='Add Run | kCalTracker'
        )
    finally:
        session.close()


@app.route('/my-runs')
def my_runs():
    """
    Path through which users get info on their runs
    """
    db = Database()
    session = db.get_session()
    runs = session.query(RunInfo).all()
    user = session.query(UserInfo).one_or_none()

    # Could potentially be done in a separate thread and passed asynchronously to frontend
    # if I was any good at AJAX wizardry.
    run_data = calculate_run_data(runs, user)

    session.close()
    # Should be able to implement paged response by limiting the number of returned runs, and by limiting the number of
    # runs which we read from the DB.
    return render_template('my_runs.html', runs=run_data, has_more_runs=False, page_title='My Runs | kCalTracker')


def calculate_run_data(runs, user):
    run_data = []
    for run in runs:
        date = run.date
        time = run.time_h
        distance = run.distance_km
        (kcals, _) = calculate_kcal(user.weight_kg, distance, time)
        run_data.append(
            {
                'date': date,
                'time': time,
                'distance': distance,
                'kcals': kcals
            }
        )
    return run_data


def get_index():
    """
    Handles get requests to index
    """
    db = Database()
    session = db.get_session()
    try:
        user_info = session.query(UserInfo).one_or_none()
        if user_info:
            return my_runs()
        else:
            return render_template('new_user.html', page_title='New User | kCalTracker')
    except MultipleResultsFound:
        session.rollback()
    finally:
        session.close()


def post_index():
    """
    Handles post request for index
    """
    username = request.form.get('username')
    weight = float(request.form.get('weight'))
    if username is None or weight is None or weight < 0:
        return render_template(
            'new_user.html',
            err='Invalid Inputs, ensure that username is set and weight is greater than 0',
            page_title='New User | kCalTracker'
        )
    db = Database()
    session = db.get_session()
    try:
        user_info = UserInfo(name=username, weight_kg=weight)
        session.add(user_info)
        session.commit()
        return my_runs()
    except InvalidRequestError as err:
        session.rollback()
        return render_template(
            'new_user.html',
            err='Failed to add user to database, please check your inputs',
            page_title='New User | kCalTracker'
        )
    finally:
        session.close()
