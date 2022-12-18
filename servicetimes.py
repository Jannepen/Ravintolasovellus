from db import db

def get_times(restaurant_id):
    sql = "SELECT * FROM servicetimes WHERE restaurant_id=(:restaurant_id)"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    times = result.fetchone()
    return times
    
def add_times(monday, tuesday, wednesday, thursday, friday, saturday, sunday, restaurant_id):
    sql = "SELECT 1 FROM servicetimes WHERE restaurant_id=(:restaurant_id)"
    check = db.session.execute(sql, {"restaurant_id":restaurant_id})
    if check:
        delete_times(restaurant_id)
    sql = "INSERT INTO servicetimes (monday, tuesday, wednesday, thursday, friday, saturday, sunday, restaurant_id) VALUES (:monday, :tuesday, :wednesday, :thursday, :friday, :saturday, :sunday, :restaurant_id)"
    result = db.session.execute(sql, {"monday":monday, "tuesday":tuesday, "wednesday":wednesday, "thursday":thursday, "friday":friday, "saturday":saturday, "sunday":sunday, "restaurant_id":restaurant_id})
    db.session.commit()
    
def delete_times(restaurant_id):
    sql = "DELETE FROM servicetimes WHERE restaurant_id=(:restaurant_id)"
    db.session.execute(sql, {"restaurant_id":restaurant_id})
    db.session.commit()
