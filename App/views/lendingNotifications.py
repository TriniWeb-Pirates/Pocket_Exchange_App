from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    createNotification,
    notifyUsers,
    getAllNotifications
)

lendingNotification_views = Blueprint('lendingNotification_views', __name__, template_folder='../templates')


#Test Routes
@lendingNotification_views.route('/testCreateLendingNotificationPage',methods=['POST'])
@login_required
def testMakeNotificationPage():
    data=request.json
    #message="Sorry but the item you have requested is unavailable at this time, Please try again when it is made available "
    notification=createNotification(data['userID'], data['requestID'], data['itemID'])
    #notification=createNotification(data['userID'], data['itemID'])
    return jsonify(notification.itemID)

@lendingNotification_views.route("/testSendNotifications/<subscriberList>/<lendingoffer_ID>", methods=['GET'])
@login_required
def testSendNotifications(subscriberList,lendingoffer_ID):
    data=request.json
    notification=notifyUsers(data['subscriberList'],data['lendingoffer_ID'])
    #code to redirect user to some page
    return jsonify(notification.userID)

@lendingNotification_views.route("/testRetrieveNotifications", methods=['GET'])
@login_required
def testGetData():
    notifications=getAllNotifications()
    #code to redirect user to some page
    return jsonify(notifications)


@lendingNotification_views.route('/notifications', methods=['GET'])
@login_required
def getNotificationPage():
    return render_template('notificationsPage.html')