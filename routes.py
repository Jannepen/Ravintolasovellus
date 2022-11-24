from app import app
from flask import redirect, render_template, request
import restaurants, reviews

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
    
@app.route("/review")
def review():
    return render_template("review.html")

@app.route("/addreview", methods=["POST"])
def addreview():
    restaurant_name = request.form["name"]
    restaurant_id = restaurants.get_id(restaurant_name)
    grade = request.form["grade"]
    message = request.form["message"]
    reviews.add_review(grade, message, restaurant_id) 
    restaurants.update_grade(restaurant_id)
    return redirect("/")

