from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_bootstrap import Bootstrap
from forms import LoginForm, ContactsForm
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'teste'
app.config['SECRET_KEY'] = '200235464'

mysql = MySQL(app)




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

@app.route("/login",methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('results.html', email=form.email.data, password= form.password.data, username=form.username.data)
    return render_template("login.html", form=form)

    

    
if __name__ == "__main__":
    app.run(debug=True)





