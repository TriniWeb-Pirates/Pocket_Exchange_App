from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    createNotification,
    notifyUsers
)

lendingNotification_views = Blueprint('lendingNotification_views', __name__, template_folder='../templates')


#Test Routes
@lendingNotification_views.route('/testCreateLendingNotificationPage',methods=['POST'])
@login_required
def testMakeNotificationPage():
    data=request.json
    message="Sorry but the item you have requested is unavailable at this time, Please try again when it is made available "
    print(data)
    notification=createNotification(data['userID'], data['requestID'], data['itemID'],data['notification'])
    return jsonify(notification.itemID)
