from App.models import BlockedUser,User
from App.database import db

#Funtion for adding blocked users to the database
def addBlackListedUser(email,phoneNumber):
    blockedUser = BlockedUser(email=email,phoneNumber=phoneNumber)
    db.session.add(blockedUser)
    db.session.commit()
    return blockedUser

def getAllBlockedUsersJSON():
    users=BlockedUser.query.all()
    info = [user.toJSON() for user in users]
    return info