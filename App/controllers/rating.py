from App.models import Rating,User
from App.database import db

def createRating(recipientID,rate):
    response = Rating(recipientID=recipientID,rate=rate)
    db.session.add(response)
    db.session.commit()
    return response

def retieveAllRatings():
    data=Rating.query.all()
    ratings = [rate.toJSON() for rate in data]
    return ratings

def updateRating(id,rate):
    rating=Rating.query.filter_by(id=id).first()
    rating.rate=rate
    db.session.add(rating)
    db.session.commit()
    return rating