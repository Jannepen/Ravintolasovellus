from db import db
import reviews

def get_list():
    sql = "SELECT name FROM restaurants"
    result = db.session.execute(sql)
    restaurants = result.fetchall()
    return restaurants

def get_gradedlist():
    sql = "SELECT name FROM restaurants ORDER BY grade DESC"
    result = db.session.execute(sql)
    restaurants = result.fetchall()
    return restaurants

def add_restaurant(name):
    sql = "INSERT INTO restaurants (name) VALUES (:name)"
    db.session.execute(sql, {"name":name})
    db.session.commit()

def delete_restaurant(name):
    sql = "DELETE FROM restaurants WHERE name=(:name)"
    db.session.execute(sql, {"name":name})
    db.session.commit()

def get_id(name):
    sql = "SELECT id FROM restaurants WHERE name=(:name)"
    result = db.session.execute(sql, {"name":name})
    restaurant_id = result.fetchone().id
    return restaurant_id

def update_grade(restaurant_id):
    grade = round(float(reviews.get_grade(restaurant_id)),1)
    sql = "UPDATE restaurants SET grade=(:grade) WHERE id=(:restaurant_id)"
    db.session.execute(sql, {"grade":grade, "restaurant_id":restaurant_id})
    db.session.commit()

def get_grade(name):
    sql = "SELECT grade FROM restaurants WHERE name=(:name)"
    result = db.session.execute(sql, {"name":name})
    restaurant_grade = result.fetchone().grade
    return restaurant_grade
