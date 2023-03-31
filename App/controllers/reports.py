from App.models import Report,BlockedUser,User
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