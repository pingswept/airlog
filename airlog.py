import time
import board
import busio
import adafruit_scd30
from flask import Flask

i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

app = Flask(__name__)

@app.route("/")
def test_concentration():
    return "<p>CO2 concentration is %d PPM.</p>" % scd.CO2
