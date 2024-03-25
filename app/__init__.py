from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_whooshee import Whooshee
from flask_mail import Mail
from flask_toastr import Toastr

import MySQLdb

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
whooshee = Whooshee(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
mail = Mail(app)
toastr = Toastr(app)

from app import routes, models

