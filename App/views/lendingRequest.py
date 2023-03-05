from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    create_lendingRequest, 
    get_request_by_ID
)

lendingRequests_views = Blueprint('lendingRequests_views', __name__, template_folder='../templates')

#testing routes
@lendingRequests_views.route('/testCreatelendingRequest',methods=['POST'])
@login_required
def makeLendingRequestPage():
    data=request.json#must change json to form for web page
    lendRequest=create_lendingRequest(data['lenderID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['returnDate'],data['borrowDate'])
    print(lendRequest.borrowDate)
    return jsonify(lendRequest.borrowDate)