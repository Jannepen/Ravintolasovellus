from app import app
from flask import redirect, render_template, request
import restaurants, reviews, users

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
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return render_template("loggedin.html", message=username)
        else:
            return render_template("error.html", message="Väärä käyttäjätunnus tai salasana")
            
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Sanasalat eroavat, yritä uudelleen.")
        if users.register(username, password1):
            return render_template("registered.html")
        else:
            return render_template("error.html", message="Rekisteröinti epäonnistui.")
    
@app.route("/logout")
def logout():
    if users.user_id():
        users.logout()
    else:
        return render_template("error.html", message="Et ole kirjautunut sisään.")
    return render_template("logout.html")
    
    
    
    

