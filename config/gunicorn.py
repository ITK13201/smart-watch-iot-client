import os
from config.config import PORT, LOGGING, BASE_DIR

wsgi_app = os.environ["FLASK_APP"]
bind = "0.0.0.0:{}".format(PORT)
proc_name = "smart-watch-iot-client"
workers = 1
accesslog = os.path.join(BASE_DIR, "log", "app.log")
errorlog = os.path.join(BASE_DIR, "log", "err.log")
logconfig_dict = LOGGING
pidfile = os.path.join(BASE_DIR, "app.pid")
daemon = True
