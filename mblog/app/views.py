from app import app
from flask import render_template,flash,redirect
from forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Thai'}
    posts = [
        {
            'author':{'nickname':'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Sunshine Apartment',
        posts = posts,
        user = user)
@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
        title = 'Sign In',
        form = form)
