"""A simple flask web app"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.history_controller import HistoryController


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    """A simple flask web app"""
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    """A simple flask web app"""
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    """A simple flask web app"""
    return CalculatorController.post()

@app.route("/history", methods=["GET"])
def table_get():
    """A simple flask web app"""
    return HistoryController.get()

@app.route("/pylint")
def pytest():
    """A simple flask web app"""
    return render_template('pylint.html')

@app.route("/testing")
def pylint():
    """A simple flask web app"""
    return render_template('testing.html')

@app.route("/oop")
def oop():
    """A simple flask web app"""
    return render_template('oop.html')

@app.route("/pattern")
def glossary():
    """A simple flask web app"""
    return render_template('pattern.html')
