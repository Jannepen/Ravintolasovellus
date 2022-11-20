from app import app
from flask import redirect, render_template, request
from db import db

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/restaurants")
def restaurants():
    sql = "SELECT name FROM restaurants"
    result = db.session.execute(sql)
    return render_template("restaurants.html", restaurants=result)


