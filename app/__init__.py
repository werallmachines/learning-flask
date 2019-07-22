#!/usr/bin/env python

from flask import Flask

application = Flask(__name__) # instance of Flask class is our app

from app import routes
