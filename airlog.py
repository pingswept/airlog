import time
import board
import busio
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test_concentration():
    return render_template('index.htm')

