from db import db
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_hex

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = token_hex(16)
            return True
        else:
            return False

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def username():
    return session.get("username")

def user_id():
    return session.get("user_id", 0)

def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]
