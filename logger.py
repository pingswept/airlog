# SPDX-FileCopyrightText: 2020 by Bryan Siepert, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
import board
import busio
import adafruit_scd30
import sqlite3
import datetime as dt
import pytz

# SCD-30 has tempremental I2C with clock stretching, datasheet recommends
# starting at 50KHz
i2c = busio.I2C(board.SCL, board.SDA, frequency=50000)
scd = adafruit_scd30.SCD30(i2c)

tz = pytz.timezone('America/New_York')
con = sqlite3.connect('../airlog.db')
cur = con.cursor()

while True:
    # since the measurement interval is long (2+ seconds) we check for new data before reading
    # the values, to ensure current readings.
    if scd.data_available:
        print("Data Available!")
        print("CO2: %d PPM" % scd.CO2)
        print("Temperature: %0.2f degrees C" % scd.temperature)
        print("Humidity: %0.2f %% rH" % scd.relative_humidity)
        print("")
        print("Waiting for new data...")
        print("")
        db_write_cmd = 'INSERT INTO readings VALUES ("{0}", {1}, {2}, {3})'.format(dt.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"), scd.CO2, scd.temperature, scd.relative_humidity)
        print(db_write_cmd)
        cur.execute(db_write_cmd)
        con.commit()

    time.sleep(15)
