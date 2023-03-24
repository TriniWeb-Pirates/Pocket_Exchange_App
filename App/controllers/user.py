from App.models import User,BlockedUser
from App.database import db

def create_user(username, password,firstName,lastName,email,phone,city,biography,links,profile_pic,picName,mimetype):
    blockedUsers=BlockedUser.query.all()
    found=False
    blockedList = [blockedUser.toJSON() for blockedUser in blockedUsers]
    for person in blockedList:
        if(person['email']==email or person['phoneNumber']==phone):
            found=True
    if(found==False):
        newuser = User(username=username, password=password,firstName=firstName,lastName=lastName,email=email,phoneNumber=phone,city=city,Bio=biography,links=links,profile_pic=profile_pic,picName=picName,mimetype=mimetype)
        db.session.add(newuser)
        db.session.commit()
        return newuser
    else:
        return "You are a blocked user"

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_phoneNumber(phoneNumber):
    return User.query.filter_by(phoneNumber=phoneNumber).first()

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

def update_user(id,username,password,firstName,lastName,email,phoneNumber,city,Bio,links,profile_pic,picName,mimetype):
    user = get_user(id)
    if user:
        user.username = username
        user.password = password
        user.firstName = firstName
        user.lastName = lastName
        user.email = email
        user.phoneNumber = phoneNumber
        user.city = city
        user.Bio = Bio
        user.links = links
        user.profile_pic = profile_pic
        user.picName = picName
        user.mimetype = mimetype
        db.session.add(user)
        db.session.commit()
        return user
    return None
    