from App.models import User
from App.database import db

def create_user(username, password,firstName,lastName,email,phone,city,biography,links,profile_pic,picName,mimetype):
    newuser = User(username=username, password=password,firstName=firstName,lastName=lastName,email=email,phoneNumber=phone,city=city,Bio=biography,links=links,profile_pic=profile_pic,picName=picName,mimetype=mimetype)
    print(newuser)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    