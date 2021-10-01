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

Set up passwordless login

```
ssh-keygen
ssh-copy-id pi@air1.nolop.org
```

Useful ad hoc ansible commands
```
ansible -u pi -i hosts.ini air -m ping
ansible -i hosts.ini air -m git_config -a "name=user.name scope=global value='Brandon Stafford'" -u pi
(same for email, but with user.email)
ansible -i hosts.ini air -m git -a "repo=git@github.com:pingswept/airlog.git dest=/home/pi/airlog update=yes clone=no" -u pi
```
