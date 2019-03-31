#!/usr/bin/env python

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # protect against CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'W8AZuJaXYWUWpysxVJdV9UbDxLDLZeor'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
