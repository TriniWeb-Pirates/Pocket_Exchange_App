from App.models import TempUser
from App.database import db

def create_temp_user(username, firstName, lastName, password, email):
    temp_user = TempUser(username=username, firstName=firstName, lastName=lastName, password=password, email=email)
    print(temp_user)
    db.session.add(temp_user)
    db.session.commit()
    return temp_user

def get_temp_user_by_username(username):
    return TempUser.query.filter_by(username=username).first()

def get_temp_user_by_email(email):
    return TempUser.query.filter_by(email=email).first()

def get_temp_user(id):
    return TempUser.query.get(id)

def get_all_temp_users():
    return TempUser.query.all()


