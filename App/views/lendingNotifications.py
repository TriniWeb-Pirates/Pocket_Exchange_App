from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    createNotification,
    notifyUsers,
    getAllNotifications,
    findBorrowingDays,
    getReturnDate,
    getAllUserLendingNotifications,
    getAllUserReportNotifications,
    deleteNotification
)

lendingNotification_views = Blueprint('lendingNotification_views', __name__, template_folder='../templates')

@lendingNotification_views.route('/notifications', methods=['GET'])
@login_required
def getNotificationPage():
    lendingNotifications=getAllUserLendingNotifications(current_user.id)
    print(lendingNotifications)
    if(type(lendingNotifications)==str):
        flash('You have no current Lending Notifications.')
        lendingNotifications=None

    reportNotifications=getAllUserReportNotifications(current_user.id)

    if(type(reportNotifications)==str):
        flash('You have no current Report Notifications.')
        reportNotifications=None
    
    return render_template('notificationsPage.html',lendingNotifications=lendingNotifications,reportNotifications=reportNotifications)


@lendingNotification_views.route('/DeleteLendingNotification/<notificationID>',methods=['POST'])
@login_required
def deleteLendingNotification(notificationID):
    
    msg = deleteNotification(notificationID)
    flash(msg)
    
    return redirect(url_for('lendingNotification_views.getNotificationPage'))





@lendingNotification_views.route('/CreateLendingNotification',methods=['POST'])
@login_required
def MakeNotification():
    #message="Sorry but the item you have requested is unavailable at this time, Please try again when it is made available "
    notification=createNotification(data['userID'], data['requestID'], data['itemID'])
    #notification=createNotification(data['userID'], data['itemID'])
    return jsonify(notification.itemID)

@lendingNotification_views.route("/SendNotifications/<subscriberList>/<lendingoffer_ID>", methods=['GET'])
@login_required
def SendNotifications(subscriberList,lendingoffer_ID):
    #data=request.json
    notification=notifyUsers(subscriberList, lendingoffer_ID)
    #code to redirect user to some page
    #return jsonify(notification.userID)
    print(notification)
    return redirect(url_for('lendingOffer_views.RetreiveAllUserOffers'))

@lendingNotification_views.route("/RetrieveNotifications", methods=['GET'])
@login_required
def GetData():
    notifications=getAllNotifications()
    #code to redirect user to some page
    return jsonify(notifications)

#Test Routes
@lendingNotification_views.route('/testCreateLendingNotificationPage',methods=['POST'])
@login_required
def testMakeNotificationPage():
    data=request.json
    #message="Sorry but the item you have requested is unavailable at this time, Please try again when it is made available "
    notification=createNotification(data['userID'], data['itemID'],data['message'])
    #notification=createNotification(data['userID'], data['itemID'])
    return jsonify(notification.toJSON(),"Lending Notification Added")

@lendingNotification_views.route("/testSendNotifications/<subscriberList>/<lendingoffer_ID>", methods=['GET'])
@login_required
def testSendNotifications(subscriberList,lendingoffer_ID):
    data=request.json
    notification=notifyUsers(data['subscriberList'],data['lendingoffer_ID'])
    #code to redirect user to some page
    return jsonify(notification.toJSON(),"Users Have Been Notified")

@lendingNotification_views.route("/testRetrieveNotifications", methods=['GET'])
@login_required
def testGetData():
    notifications=getAllNotifications()
    #code to redirect user to some page
    return jsonify(notifications)

@lendingNotification_views.route('/TestDeleteLendingNotification',methods=['DELETE'])
@login_required
def TestdeleteLendingNotification():
    data=request.json
    msg = deleteNotification(data['notificationID'])
    return jsonify("Lending Notification Deleted")
