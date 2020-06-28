"""
Defines routes for the WSGI application
"""
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    """
    Default path for web application
    """
    # If no user defined create a new one and request name and weight
    return render_template('index.html')


@app.route('/add-data')
def add_data():
    """
    Path through which users post data
    """
    if request.method != 'POST':
        return render_template('index.html')
    # Store data in DB, reload saved data and parse inputs
    return render_template('index.html')
