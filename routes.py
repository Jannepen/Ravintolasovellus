from app import app
from flask import redirect, render_template, request
import restaurants

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    restaurants.add_restaurant(name)
    return redirect("/")

@app.route("/remove")
def remove():
    return render_template("remove.html")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form["name"]
    restaurants.delete_restaurant(name)
    return redirect("/")

@app.route("/restaurants")
def restaurants_list():
    result = restaurants.get_list()
    return render_template("restaurants.html", restaurants=result)

