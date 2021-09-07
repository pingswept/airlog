Set up wireless connection and enable SSH and I2C in `raspi-config`

```
sudo apt install libatlas-base-dev git python3-pip supervisor # don't use pip to install Supervisor
sudo pip3 install pandas flask adafruit-circuitpython-scd30
export FLASK_APP=airlog
python3 -m flask run --host=0.0.0.0
```

Add to `/etc/supervisor/supervisord.conf`:
```
[program:airlog_webserver]
directory=/home/pi/airlog
command=python3 -m flask run --host=0.0.0.0

[program:airlog_logger]
directory=/home/pi/airlog
command=python3 logger.py
```

Create database
```
import sqlite3

con = sqlite3.connect('airlog.db')
cur = con.cursor()
cur.execute('''CREATE TABLE readings (date text, co2 real, temperature real, humidity real)''')
con.commit()
con.close()
```
