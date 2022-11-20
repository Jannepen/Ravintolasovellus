from app import app
from flask import redirect, render_template, request

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/restaurants")
def restaurants():
    return render_template("restaurants.html")
