import json
from flask import Flask
import platform
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'klchJ89Bch'

os_info = platform.system()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('users.json') as f:
    users = json.load(f)

app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_PERMANENT'] = True

from app import views