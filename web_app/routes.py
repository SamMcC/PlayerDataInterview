"""
Defines routes for the WSGI application
"""
from flask import Flask, render_template, request
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import MultipleResultsFound

from db.user_info import UserInfo
from db.run_info import RunInfo
from db.database import Database
from maths.leger_kcal_calculator import calculate_kcal

app = Flask(__name__, template_folder='./templates')


@app.route('/', methods=['GET'])
def index():
    """
    Default path for web application
    """
    if request.method == 'POST':
        return post_index()
    return get_index()


@app.route('/add-run')
def add_data():
    """
    Path through which users post new run data
    """
    if request.method != 'POST':
        return render_template('add_run.html')
    # Store data in DB, reload saved data and parse inputs
    date = request.form.get('date')
    time = request.form.get('time')
    distance = request.form.get('distance')
    if date is None or time is None or time < 0 or distance is None or distance < 0:
        return render_template(
            'new_user.html',
            err='Invalid Inputs, ensure that date is set, and time and distance are greater than 0'
        )
    db = Database()
    session = db.get_session()
    try:
        run_info = RunInfo()
        session.add(run_info)
        session.commit()
        return render_template('my_runs.html')
    except InvalidRequestError as err:
        session.rollback()
        return render_template('add_run.html', err='Failed to add run to database, please check your inputs')
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
    run_data = []
    for run in runs:
        date = run.date
        time = run.time_h
        distance = run.distance_km
        (kcals, _) = calculate_kcal(user.weight, distance, time)
        run_data.append(
            {
                'date': date,
                'time': time,
                'distance': distance,
                'kcals': kcals
            }
        )

    session.close()
    # Should be able to implement paged response by limiting the number of returned runs
    return render_template('my_runs.html', runs=run_data, has_more_runs=False)


def get_index():
    """
    Handles get requests to index
    """
    db = Database()
    session = db.get_session()
    try:
        user_info = session.query(UserInfo).one_or_none()
        if user_info:
            return render_template("my_runs.html")
        else:
            return render_template('new_user.html')
    except MultipleResultsFound:
        session.rollback()
    finally:
        session.close()


def post_index():
    """
    Handles post request for index
    """
    username = request.form.get('name')
    weight = request.form.get('weight')
    if username is None or weight is None or weight < 0:
        return render_template(
            'new_user.html',
            err='Invalid Inputs, ensure that username is set and weight is greater than 0'
        )
    db = Database()
    session = db.get_session()
    try:
        user_info = UserInfo(name=username, weight=weight)
        session.add(user_info)
        session.commit()
        return render_template('my_runs.html')
    except InvalidRequestError as err:
        session.rollback()
        return render_template('new_user.html', err='Failed to add user to database, please check your inputs')
    finally:
        session.close()
