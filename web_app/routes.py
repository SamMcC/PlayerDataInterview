"""
Defines routes for the WSGI application
"""
from flask import Flask, render_template, request
from sqlalchemy.orm.exc import MultipleResultsFound

from db.run_info import RunInfo
from db.user_info import UserInfo
from db.database import Database

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
    """
    Default path for web application
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
