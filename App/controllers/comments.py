from App.models import Comment,User
from App.database import db

#Function for adding a comment to another user
def createComment(commentedUserID,comment):
    newComment = Comment(commentedUserID=commentedUserID,comment=comment)
    db.session.add(newComment)
    print(newComment)
    db.session.commit()
    return newComment

#Function to get all comments from a user
def getComments(commentedUserID):
    comments = Comment.query.filter_by(commentedUserID=commentedUserID).all()
    if comments:
        results = [comment.toJSON() for comment in comments]
    else:
        results=None
    print(results)
    return results