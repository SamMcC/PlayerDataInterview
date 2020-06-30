"""
Defines routes for the WSGI application
"""
from flask import Flask, render_template, request
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import MultipleResultsFound

from db.user_info import UserInfo
from db.run_info import RunInfo
from db.database import Database

app = Flask(__name__, template_folder='./templates')


@app.route('/', methods=['GET'])
def index():
    """
    Default path for web application
    """
    if request.method == 'POST':
        return post_index()
    return get_index()


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
        user_info = UserInfo()
        session.add(user_info)
        session.commit()
        return render_template('my_runs.html')
    except InvalidRequestError as err:
        session.rollback()
        return render_template('new_user.html', err='Failed to add user to database, please check your inputs')
    finally:
        session.close()


@app.route('/add-run')
def add_data():
    """
    Path through which users post data
    """
    if request.method != 'POST':
        return render_template('add-run.html')
    # Store data in DB, reload saved data and parse inputs
    return my_runs()


@app.route('/my-runs')
def my_runs():
    """
    Path through which users post data
    """
    return render_template('my-runs.html')
