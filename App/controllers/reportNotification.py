from App.models import ReportNotification,User
from App.database import db

message="Warning someone has filed a report against you, if you are reported "
message2=" time/s your account will be deleted!"


def createReportNotification(userID):
    user=User.query.get(userID)
    num=5-user.reportsCount
    remainder=str(num)
    reportNotification=ReportNotification(userID=userID, notification=message+remainder+message2)
    db.session.add(reportNotification)
    db.session.commit()
    return reportNotification.toJSON()

def getAllUserReportNotifications(userID):
    messages=ReportNotification.query.filter_by(userID=userID).all()
    if(messages):
        notifications = [message.toJSON() for message in messages]
        return notifications
    else:
        return "You currently have no Report Notifications"