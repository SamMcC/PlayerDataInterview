from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-data', methods=['POST'])
def index():
    return render_template('index.html')
