from App.models import TempUser
from App.database import db

#Function to create a temp user 
def create_temp_user(username, firstName, lastName, password, email):
    temp_user = TempUser(username=username, firstName=firstName, lastName=lastName, password=password, email=email)
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
    temp_users = TempUser.query.all()
    if(temp_users):
        return temp_users
    else:
        return None

    
def get_all_temp_users_json():
    temp_users = TempUser.query.all()
    if not temp_users:
        return []
    temp_users = [temp_user.toJSON() for temp_user in temp_users]
    return temp_users

#Function to delete a temp user
def delete_temp_user(id):
    temp_user = get_temp_user(id)
    db.session.delete(temp_user)
    db.session.commit()

def update_temp_user(id, username, firstName, lastName, password, email):
    temp_user = get_temp_user(id)
    if(temp_user):
        temp_user.username = username
        temp_user.firstName = firstName
        temp_user.lastName = lastName
        temp_user.password = password
        temp_user.email = email
        db.session.add(temp_user)
        db.session.commit()
        return temp_user
    else:
        return None



