from app import app
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_bootstrap import Bootstrap
from app.forms import LoginForm, RegistrationForm


@app.route('/', methods=['GET', 'POST'])
def index():
       return render_template('index.html')
    
@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/gameslist")
def gameslist():
    return render_template("gameslist.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.uti_nome.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)