from db import db

def get_list():
    sql = "SELECT name FROM restaurants"
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
