import time
import pandas as pd
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test_concentration():
    con = sqlite3.connect("airlog.db")
    df = pd.read_sql_query("SELECT * FROM readings", con)

    con.close()

    timestamps = df['date'].values.tolist()
    data = df['co2'].values.tolist()

    return render_template('index.htm', timestamps=timestamps, data=data)
