from App.models import Report,BlockedUser,User,ReportNotification
from App.database import db

def create_report(userID,offenderID,description):
    user=User.query.get(offenderID)
    if(userID!=offenderID):
        report = Report(offenderID=offenderID,description=description)
        user.reportsCount=user.reportsCount+1
        db.session.add(report)
        db.session.commit()
        db.session.add(user)
        db.session.commit()
        createReportNotification(offenderID)
        #reports=Report.query.filter_by(offenderID=offenderID).all()
        #data = [report.toJSON() for report in reports]
        #count=0
        #for item in data:
        #    count=count+1
        if(user.reportsCount>=3):
            blackListedUser=addBlackListedUser(user.email,user.phoneNumber)
            db.session.add(blackListedUser)
            db.session.commit()
            db.session.delete(user)
            db.session.commit()
            return report.toJSON()
        else:
            return report.toJSON()
    else:
        return "Action denied, user cannot report themselves"

        
 

def get_report_by_ID(reportID):
    return Report.query.filter_by(reportID=reportID).first()

def get_offender(offenderID):
    return Report.query.get(offenderID)

def get_all_reports():
    return Report.query.all()

def addBlackListedUser(email,phoneNumber):
    blockedUser = BlockedUser(email=email,phoneNumber=phoneNumber)
    db.session.add(blockedUser)
    db.session.commit()
    return blockedUser

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