from flask import render_template, flash, redirect, url_for, request 
from app import application
from flask_login import current_user, login_user, logout_user, login_required # import Flask-Login
from werkzeug.urls import url_parse
from app.models import User # import User model
from app.forms import LoginForm

@application.route('/')
@application.route('/index')
@login_required
def index():
    posts = [{'author': {'username': 'John'},
              'body': 'Beautiful day in Portland!'},
             {'author': {'username': 'Susan'},
               'body': 'The Avengers movie sucked'},
              {'author': {'username': 'Zayda'},
                'body': 'I dunno what to do'}]

    return render_template('index.html', title='Home', posts=posts)

@application.route('/login', methods=['GET', 'POST'])
def login():
    # if already logged in, bounce to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # this is the actual login functionality
    if form.validate_on_submit(): # validates input, returns True
        # query for user
        user = User.query.filter_by(username=form.username.data).first()
        # check if user exists, or password incorrect
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
            # this function comes from Flask-Login
        login_user(user, remember=form.remember_me.data)
        # for REQUIRED login, get the next=<view> argument
        # flask.request.args.get returns query string as dict obj
        next_page = request.args.get('next') 
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('successful_login'))

    return render_template('login.html', title='Sign In', form=form)

@application.route('/successful_login')
def successful_login():
    return render_template('successful_login.html', user=current_user.username)

@application.route('/logout')
def logout():
    # below is flask_login method, similar to login_user
    logout_user() 
    return redirect(url_for('index'))
