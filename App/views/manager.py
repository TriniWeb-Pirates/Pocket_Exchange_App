from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    addToList,
    getList
)

manager_views = Blueprint('manager_views', __name__, template_folder='../templates')

#Testing Routes
@manager_views.route('/addToList/<borrowerID>/<lendingoffer_ID>', methods=['POST'])
@login_required
def testAddUsersToList(borrowerID,lendingoffer_ID):
    interestedUsers=addToList(borrowerID, lendingoffer_ID)
    pass
    #return redirect(url_for(""))

@manager_views.route('/testSendList/<lendingoffer_ID>', methods=['GET'])
@login_required
def testTransmitList(lendingoffer_ID):
    subscriberList=getList(lendingoffer_ID)
    pass
    #return redirect(url_for())