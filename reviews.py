from db import db

def add_review(grade, message, restaurant_id):
    sql = """INSERT INTO reviews (grade, message, restaurant_id, sent_at)
          VALUES (:grade, :message, :restaurant_id, NOW())"""
    db.session.execute(sql,{"grade":grade, "message":message, "restaurant_id":restaurant_id})
    db.session.commit()

def get_grade(restaurant_id):
    sql = "SELECT AVG(ALL grade) FROM reviews WHERE restaurant_id=(:restaurant_id)"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    average = result.fetchone()[0]
    return average

def get_reviews(restaurant_id):
    sql = "SELECT grade, message, sent_at FROM reviews WHERE restaurant_id=(:restaurant_id)"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    reviews = result.fetchall()
    return reviews
