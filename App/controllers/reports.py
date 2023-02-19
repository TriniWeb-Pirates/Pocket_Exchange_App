from App.models import Report
from App.database import db

def create_report(offenderID,description):
    report = Report(offenderID=offenderID,description=description)
    db.session.add(report)
    db.session.commit()
    return report

def get_report_by_ID(reportID):
    return Report.query.filter_by(reportID=reportID).first()

def get_offender(offenderID):
    return Report.query.get(offenderID)

def get_all_reports():
    return Report.query.all()