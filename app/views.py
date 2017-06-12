#! coding: utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from app import app
from .forms import LoginForm

@app.route('/index')
def index():
    user = {'nickname': 'Mike'}
    posts = [
        {
            'author': {'nickname': 'Mike'},
            'body': 'Nice day!'
        },
        {
            'author': {'nickname': 'Su'},
            'body': 'So cool!'
        }
    ]
    return render_template("index.html",
    title = 'Home',
    user = user,
    posts = posts
    )

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template("login.html",
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
