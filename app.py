from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database.py import *


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######

@app.route('/')
def hello_world():
	return render_template("home.html")

@app.route('/store')
def hello_store():
	return render_template("store.html", products=products)

@app.route('/about')
def hello_about():
	return render_template("about.html")

@app.route('/cart')
def hello_cart():
	return render_template("cart.html")


#####################


if __name__ == '__main__':
    app.run(debug=True)