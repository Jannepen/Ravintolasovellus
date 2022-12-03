from db import db

def get_times(restaurant_id):
    sql = "SELECT * FROM servicetimes WHERE restaurant_id=(:restaurant_id)"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    times = result.fetchone()
    
    return times
