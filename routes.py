from app import app
from flask import redirect, render_template, request
import restaurants, reviews, users, servicetimes

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == "POST":
        name = request.form["name"]
        restaurants.add_restaurant(name)
        return redirect("/")

@app.route("/remove", methods=["GET", "POST"])
def remove():
    if request.method == "GET":
        result = restaurants.get_list()
        return render_template("remove.html", restaurants=result)
    if request.method == "POST":
        name = request.form["name"]
        restaurants.delete_restaurant(name)
        return redirect("/")

@app.route("/restaurants", methods=["GET", "POST"])
def restaurants_list():
    if request.method == "GET":
        result = restaurants.get_list()
        return render_template("restaurants.html", restaurants=result)
    if request.method == "POST":
        result = restaurants.get_gradedlist()
        return render_template("restaurants.html", restaurants=result)
    
@app.route("/restaurants/<string:name>")
def restaurant(name):
    restaurant_id = restaurants.get_id(name)
    restaurant_grade = restaurants.get_grade(name)
    restaurant_times = servicetimes.get_times(restaurant_id)
    restaurant_reviews = reviews.get_reviews(restaurant_id)
    return render_template("restaurant.html", restaurant=name, grade=restaurant_grade, times=restaurant_times, reviews = restaurant_reviews)
    
@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "GET":
        result = restaurants.get_list()
        return render_template("review.html", restaurants=result)
    if request.method == "POST":
        restaurant_name = request.form["name"]
        restaurant_id = restaurants.get_id(restaurant_name)
        grade = request.form["grade"]
        message = request.form["message"]
        reviews.add_review(grade, message, restaurant_id) 
        restaurants.update_grade(restaurant_id)
        return redirect("/")
        
@app.route("/servicetimes", methods=["GET", "POST"])
def addservicetimes():
    if request.method == "GET":
        result = restaurants.get_list()
        return render_template("servicetimes.html", restaurants=result)
    if request.method == "POST":
        restaurant_name = request.form["name"]
        restaurant_id = restaurants.get_id(restaurant_name)
        monday = request.form["monday"]
        tuesday = request.form["tuesday"]
        wednesday = request.form["wednesday"]
        thursday = request.form["thursday"]
        friday = request.form["friday"]
        saturday = request.form["saturday"]
        sunday = request.form["sunday"]
        servicetimes.add_times(monday, tuesday, wednesday, thursday, friday, saturday, sunday, restaurant_id)
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
    
    
    
    

