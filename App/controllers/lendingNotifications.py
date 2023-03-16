from App.models import LendingNotification,User
from App.database import db

def notifyUsers(interestedUsers):
    offer = LendingOffer(lenderID=lenderID,item=item,category=category,condition=condition,preferedLocation=preferedLocation,Status=Status,RulesOfUse=rulesOfUse)
    db.session.add(offer)
    db.session.commit()
    return offer