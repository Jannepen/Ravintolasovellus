from app import app
from flask import redirect, render_template, request
from db import db

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    sql = "INSERT INTO restaurants (name) VALUES (:name)"
    result = db.session.execute(sql, {"name":name})
    db.session.commit()
    return redirect("/")

@app.route("/restaurants")
def restaurants():
    sql = "SELECT name FROM restaurants"
    result = db.session.execute(sql)
    return render_template("restaurants.html", restaurants=result)

