#!/usr/bin/env python

from flask import Flask # import the Flask class
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

application = Flask(__name__) # instance of Flask class is our app
# get config variables set
application.config.from_object(Config)
# initiate all the Flask extensions below
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login = LoginManager(application)
# used by flask_login to REQUIRE logins for certain views, tell
# flask_login where the login view is
login.login_view = 'login'

from app import routes, models
