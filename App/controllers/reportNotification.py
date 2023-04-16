from App.models import ReportNotification,User
from App.database import db

#String variables for creating report notifications
message="Warning someone has filed a report against you, if you are reported "
message2=" more time/s your account will be deleted!"

#Function to create a report notification for a user
def makeReportNotification(userID):
    user=User.query.get(userID)
    num=3-user.reportsCount
    remainder=str(num)
    reportNotification=ReportNotification(userID=userID, notification=message+remainder+message2)
    db.session.add(reportNotification)
    db.session.commit()
    return reportNotification.toJSON()

#Function to return all report notifications for a user as a list of dicts
def getAllUserReportNotifications(userID):
    messages=ReportNotification.query.filter_by(userID=userID).all()
    if(messages):
        notifications = [message.toJSON() for message in messages]
        return notifications
    else:
        return "You currently have no Report Notifications"