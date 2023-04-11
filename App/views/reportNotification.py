from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    createReportNotification,
    getAllUserReportNotifications,
    deleteReportNotif
)

reportingNotification_views = Blueprint('reportingNotification_views', __name__, template_folder='../templates')

@reportingNotification_views.route('/CreateReportNotificationPage/<offenderID>',methods=['POST'])
@login_required
def MakeReportNotificationPage(offenderID):
    notification=createReportNotification(offenderID)
    return jsonify(notification)


@reportingNotification_views.route('/DeleteReportNotification/<notificationID>',methods=['POST'])
@login_required
def deleteReportN(notificationID):
    msg = deleteReportNotif(notificationID)
    flash(msg)
    return redirect(url_for('lendingNotification_views.getNotificationPage'))


#Test Routes
@reportingNotification_views.route('/testCreateReportNotificationPage',methods=['POST'])
@login_required
def testMakeReportNotificationPage():
    data=request.json
    notification=createReportNotification(data['userID'])
    return jsonify(notification)