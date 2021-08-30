import time
import board
import busio
import adafruit_scd30
from flask import Flask, render_template

i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

app = Flask(__name__)

@app.route("/")
def test_concentration():
    return render_template('index.htm')

#while True:
#    if scd.data_available:
#        print("CO2: %d PPM" % scd.CO2)
#    time.sleep(0.5)

