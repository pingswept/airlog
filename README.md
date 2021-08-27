```
pip3 install adafruit-circuitpython-scd30
pip3 install flask
Successfully installed Jinja2-3.0.1 MarkupSafe-2.0.1 Werkzeug-2.0.1 click-8.0.1 flask-2.0.1 importlib-metadata-4.7.1 itsdangerous-2.0.1 typing-extensions-3.10.0.0 zipp-3.5.0
export FLASK_APP=airlog
python3 -m flask run --host=0.0.0.0
apt install supervisor # don't use pip to install Supervisor
```

```
[program:airlog_webserver]
directory=/home/pi/airlog
environment=FLASK_APP="airlog.py"
command=python3 -m flask run --host=0.0.0.0

[program:airlog_logger]
directory=/home/pi/airlog
command=python3 logger.py
```
