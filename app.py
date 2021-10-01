import datetime as dt
import time
import pandas as pd
import requests
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test_concentration():
    delta = dt.timedelta(days=3)
    # generate a string that looks like this: 'http://air1.nolop.org:5000/range/2021-09-23/2021-09-25'
    addr = 'http://127.0.0.1:5000/range/' + (dt.date.today() - delta).isoformat() + '/' + dt.date.today().isoformat()
    r = requests.get(addr).json()
    return render_template('index.htm', timestamps=r['timestamps'], data=r['data'])

@app.route("/range/<startdate>/<enddate>")
def get_date_range(startdate, enddate):
    con = sqlite3.connect("airlog.db")
    df = pd.read_sql_query("SELECT * FROM readings WHERE date BETWEEN date('{0}') AND date('{1}')".format(startdate, enddate), con)
    con.close()
    d = {'timestamps': df['date'].values.tolist(), 'data': df['co2'].values.tolist()}
    return d
