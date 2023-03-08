from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    create_lendingRequest, 
    get_request_by_ID,
    updateLendingRequest,
    getAllRequestsJSON,
    countRequests
)

lendingRequests_views = Blueprint('lendingRequests_views', __name__, template_folder='../templates')

@lendingRequests_views.route('/lendingRequestForm/<id>', methods=['GET'])
@login_required
def testGetLendingRequestData(id):
    lenderID=id
    result=countRequests(lenderID)
    if result!=None:
        return redirect(url_for('user_views.gethomepage',id=id))
    return jsonify(result)
    #return render_template()


@lendingRequests_views.route('/CreatelendingRequest',methods=['POST'])
@login_required
def makeLendingRequestPage():
    data=request.form
    lendRequest=create_lendingRequest(data['lenderID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['returnDate'],data['borrowDate'])
    return jsonify(lendRequest.borrowDate)




#testing routes
@lendingRequests_views.route('/testLendingRequestForm', methods=['GET'])
@login_required
def testGetLendingRequestData():
    data=request.json
    lenderID=data['id']
    result=countRequests(lenderID)
    if result!=None:
        return jsonify(result)
        #return redirect(url_for('user_views.gethomepage',id=id))
    return jsonify(result)
    #return render_template()


@lendingRequests_views.route('/testCreatelendingRequest',methods=['POST'])
@login_required
def testMakeLendingRequestPage():
    data=request.json#must change json to form for web page
    lendRequest=create_lendingRequest(data['lenderID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['returnDate'],data['borrowDate'])
    print(lendRequest.borrowDate)
    return jsonify(lendRequest.borrowDate)

@lendingRequests_views.route('/testUpdateLendingRequest',methods=['PUT'])
@login_required
def testUpdateLendingRequestPage():
    data=request.json
    lendRequest=updateLendingRequest(data['id'],data['lenderID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['borrowDate'],data['returnDate'])
    return jsonify(lendRequest.borrowDate)

@lendingRequests_views.route('/testGetAllRequests', methods=['GET'])
@login_required
def testRetreiveAllRequests():
    requests=getAllRequestsJSON()
    return requests