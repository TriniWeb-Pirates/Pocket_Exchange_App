from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    create_lendingRequest, 
    get_request_by_ID,
    updateLendingRequest,
    getAllRequestsJSON,
    getAllUserRequestsJSON,
    countRequests,
    getAllOfferRequests,
    grantTempApproval,
    changeStatus,
    getRequest,
    UnapproveTemp,
    getAllUserOffers,
    setDates
)

lendingRequests_views = Blueprint('lendingRequests_views', __name__, template_folder='../templates')


@lendingRequests_views.route('/lendingRequestForm/<id>', methods=['GET'])
@login_required
def GetLendingRequestData(id):
    result=countRequests(current_user.id)
    if result!=None:
        flash(result)
        return redirect(url_for('user_views.gethomepage',id=current_user.id))
    return render_template('homepage.html',id=id)

#Route to capture lending request data to create lending request object
@lendingRequests_views.route('/CreatelendingRequest/<lendingoffer_ID>',methods=['POST'])
@login_required
def makeLendingRequestPage(lendingoffer_ID):
    data=request.form
    result=countRequests(current_user.id)
    if result!=None:
        flash(result)
        return redirect(url_for('user_views.gethomepage',id=current_user.id))
    lendRequest=create_lendingRequest(current_user.id,lendingoffer_ID,data['reasonForUse'],data['preferedLocation'])
    flash(lendRequest)
    #return jsonify(lendRequest)
    return redirect(url_for('manager_views.AddUsersToList',borrowerID=current_user.id,lendingoffer_ID=lendingoffer_ID))

@lendingRequests_views.route('/updateLendingRequestForm/<id>', methods=['GET'])
@login_required
def GetLendingRequest(id):
    request=getRequest(id)
    return render_template('homepage.html',request=request,id=id)

@lendingRequests_views.route('/UpdateLendingRequest/<id>/<lendingoffer_ID>',methods=['PUT'])
@login_required
def UpdateLendingRequestPage(id,lendingoffer_ID):
    data=request.form
    lendRequest=updateLendingRequest(id,current_user.id,lendingoffer_ID,data['reasonForUse'],data['preferedLocation'])
    return redirect(url_for(''))

@lendingRequests_views.route('/GetAllRequests', methods=['GET'])
@login_required
def RetreiveAllRequests():
    requests=getAllRequestsJSON()
    return jsonify(requests)

@lendingRequests_views.route('/GetAllOfferRequests/<lendingoffer_ID>', methods=['GET'])
@login_required
def RetreiveOfferRequests(lendingoffer_ID):
    requests=getAllOfferRequests(lendingoffer_ID)
    return jsonify(requests)

@lendingRequests_views.route('/GrantTempApproval/<lendingRequestID>/<lendingoffer_ID>', methods=['POST'])
@login_required
def GrantTempApproval(lendingRequestID,lendingoffer_ID):
    data=request.form
    lendingRequest=grantTempApproval(lendingRequestID,lendingoffer_ID,current_user.id)
    offers=getAllUserOffers(current_user.id)
    #return jsonify(lendingRequest)#redirect user to setDates route with ID of approved lending request
    flash('You have successfully granted this user temporary approval.')
    return render_template("myLendingOffers.html", offers=offers)


@lendingRequests_views.route('/GrantTempApproval2/<lendingRequestID>/<lendingoffer_ID>', methods=['POST'])
@login_required
def GrantTempApproval2(lendingRequestID,lendingoffer_ID):
    data=request.form
    lendingRequest=grantTempApproval(lendingRequestID,lendingoffer_ID,current_user.id)
    offers=getAllUserOffers(current_user.id)
    #return jsonify(lendingRequest)#redirect user to setDates route with ID of approved lending request
    flash('You have successfully granted this user temporary approval. You can see the status of your offer in the My Items Page > My Lending Items')
    return redirect(url_for('user_views.gethomepage'))

   # return redirect(url_for('lendingOffer_views.InputDates'),id=lendingRequest.id,borrowerID=request.borrowerID,lendingoffer_ID=request.lendingoffer_ID)

@lendingRequests_views.route('/UnApproveTempApproval/<lendingRequestID>',methods=['POST'])
@login_required
def UnApproval(lendingRequestID):
    #data=request.form
    lendRequest=UnapproveTemp(lendingRequestID,current_user.id)
    flash('You have cancelled this users temporary approval request. Your offer will be re-displayed in the homepage. ')
    return redirect(url_for('lendingOffer_views.RetreiveAllUserOffers'))

#Route for changing request status
@lendingRequests_views.route('/ChangeStatus/<lendingRequestID>/<lendingoffer_ID>', methods=['POST'])
@login_required
def StatusChange(lendingRequestID, lendingoffer_ID):
    data=request.form
    offer=setDates(lendingoffer_ID,lendingRequestID,data['returnDate'],data['borrowDate'])
    lendingRequest=changeStatus(lendingRequestID,current_user.id)
    return redirect(url_for('manager_views.TransmitList',lendingoffer_ID=lendingoffer_ID))
    #return redirect(url_for(),borrowerID=request.borrowerID,lendingoffer_ID=request.lendingoffer_ID,)


@lendingRequests_views.route('/GetAllUserRequests', methods=['GET'])
@login_required
def getUserRequests():

    requests = getAllUserRequestsJSON(current_user.id)

    return render_template('myBorrowRequests.html', requests=requests)


#testing routes
#Route to test lending request limit in Postman
@lendingRequests_views.route('/testLendingRequestForm', methods=['GET'])
@login_required
def testGetLendingRequestData():
    data=request.json
    borrowerID=data['id']
    result=countRequests(borrowerID)
    if result!=None:
        return jsonify(result)
        #return redirect(url_for('user_views.gethomepage',id=id))
    return jsonify(result)
    #return render_template()

#Route to test creating a lending request 
@lendingRequests_views.route('/testCreatelendingRequest',methods=['POST'])
@login_required
def testMakeLendingRequestPage():
    data=request.json#must change json to form for web page
    lendRequest=create_lendingRequest(data['borrowerID'],data['lendingoffer_ID'],data['reasonForUse'],data['preferedLocation'])
    #print(lendRequest.borrowDate)
    return jsonify(lendRequest)
    #return redirect(url_for("manager_views.testAddUsersToList"),borrowerID=data['borrowerID'],lendingoffer_ID=data['lendingoffer_ID'])
    #Code to redirect user to manager views to add user to list

#Route to test updating lending request object
@lendingRequests_views.route('/testUpdateLendingRequest',methods=['PUT'])
@login_required
def testUpdateLendingRequestPage():
    data=request.json
    lendRequest=updateLendingRequest(data['id'],data['borrowerID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['tempApproval'])
    return jsonify(lendRequest.borrowDate)

@lendingRequests_views.route('/testUnApproveTempApproval',methods=['PUT'])
@login_required
def testUnApproval():
    data=request.json
    lendRequest=UnapproveTemp(data['lendingRequestID'],current_user.id)
    return lendRequest

#Route to test retrieving all lending request objects in the database
@lendingRequests_views.route('/testGetAllRequests', methods=['GET'])
@login_required
def testRetreiveAllRequests():
    requests=getAllRequestsJSON()
    return requests

#Route to test retrieving all lending request objects in the database
@lendingRequests_views.route('/testGetAllUserRequests/<borrowerID>', methods=['GET'])
@login_required
def testRetreiveAllUserRequests(borrowerID):
    requests=getAllUserRequestsJSON(borrowerID)
    return requests


#Route for retrieving all requests for an offer
@lendingRequests_views.route('/testGetAllOfferRequests/<lendingoffer_ID>', methods=['GET'])
@login_required
def testRetreiveOfferRequests(lendingoffer_ID):
    requests=getAllOfferRequests(lendingoffer_ID)
    return jsonify(requests) 

#Route for granting temporary approval
@lendingRequests_views.route('/testGrantTempApproval', methods=['PUT'])
@login_required
def testGrantTempApproval():
    data=request.json
    lendingRequest=grantTempApproval(data['id'],data['lendingoffer_ID'],current_user.id,data['status'])
    return jsonify(lendingRequest)#redirect user to setDates route with ID of approved lending request
    #return redirect(url_for(),borrowerID=request.borrowerID,lendingoffer_ID=request.lendingoffer_ID,)

#Route for changing request status
@lendingRequests_views.route('/testChangeStatus', methods=['PUT'])
@login_required
def testStatusChange():
    data=request.json
    lendingRequest=changeStatus(data['id'],current_user.id,data['status'])
    return jsonify(lendingRequest)
    #return redirect(url_for(),borrowerID=request.borrowerID,lendingoffer_ID=request.lendingoffer_ID,)

