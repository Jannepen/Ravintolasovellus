from db import db

def add_group(restaurant_id, groupname):
    sql = """INSERT INTO groups (restaurant_id, groupname)
          VALUES (:restaurant_id, :groupname)"""
    db.session.execute(sql,{"restaurant_id":restaurant_id, "groupname":groupname})
    db.session.commit()

def get_groups(restaurant_id):
    sql = "SELECT groupname FROM groups WHERE restaurant_id=(:restaurant_id)"
    result = db.session.execute(sql, {"restaurant_id":restaurant_id})
    groups = result.fetchall()
    return groups
