import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '1Q'
# sqlite:////home/mgu/Python/thermos/thermos-flask/thermos.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# @TODO Debug for manage.py runserver
app.config['DEBUG'] = True

db = SQLAlchemy(app)

# Configure authentification
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.init_app(app)


# @TODO for debug mode
from logging import DEBUG
app.logger.setLevel(DEBUG)

import models
import views




