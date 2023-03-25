from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    addToList,
    getList
)

manager_views = Blueprint('manager_views', __name__, template_folder='../templates')

@manager_views.route('/AddToList/<borrowerID>/<lendingoffer_ID>', methods=['POST'])
@login_required
def AddUsersToList(borrowerID,lendingoffer_ID):
    #data=request.json
    interestedUsers=addToList(borrowerID, lendingoffer_ID)
    #return jsonify(interestedUsers.InterestedUserList)
    return redirect(url_for("user_views.gethomepage"))

@manager_views.route('/SendList/<lendingoffer_ID>', methods=['GET'])
@login_required
def TransmitList(lendingoffer_ID):
    #data=request.json
    subscriberList=getList(lendingoffer_ID)
    #return jsonify(subscriberList.InterestedUserList)
    return redirect(url_for('lendingNotification_views.SendNotifications'),subscriberList=subscriberList,lendingoffer_ID=lendingoffer_ID)

#Testing Routes
@manager_views.route('/testAddToList/<borrowerID>/<lendingoffer_ID>', methods=['POST'])
@login_required
def testAddUsersToList(borrowerID,lendingoffer_ID):
    data=request.json
    interestedUsers=addToList(data['borrowerID'], data['lendingoffer_ID'])
    return jsonify(interestedUsers.InterestedUserList)
    #return redirect(url_for(""))

@manager_views.route('/testSendList/<lendingoffer_ID>', methods=['GET'])
@login_required
def testTransmitList(lendingoffer_ID):
    data=request.json
    subscriberList=getList(data['lendingoffer_ID'])
    return jsonify(subscriberList.InterestedUserList)
    #return redirect(url_for(),lendingoffer_ID=lendingoffer_ID)