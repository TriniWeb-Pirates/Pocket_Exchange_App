from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
#from flask_jwt import jwt_required, current_identity

from.index import index_views

from App.controllers import (
    create_user,
    get_user_by_username, 
    get_all_users,
    get_all_users_json,
    login_user,
    authenticate
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

#testing route
@user_views.route('/testAddUser',methods=['POST'])
def testAddUser():
    data1=request.json
    user=get_user_by_username(data1['username'])
    if user:
        flash("Username is taken please enter a new username.")
        return jsonify("Username is taken please enter a new username.")
    user=create_user(data1['username'], data1['password'], data1['firstName'], data1['lastName'], data1['phoneNumber'],data1['email'], data1['city'], data1['Bio'], data1['links'])
    print(user.firstName)
    return jsonify(user)


@user_views.route('/signupPage1', methods=['GET'])
def getSignupPage1():
    pass
    #return render_template()

@user_views.route('/add_User_Page1',methods=['POST'])
def create_user_page1():
    data1=request.form
    user=get_user_by_username(data1['username'])
    if user:
        flash("Username is taken please enter a new username.")
        #return jsonify("Username is taken please enter a new username.")
    #user=create_user(data['username'], data['password'], data['firstName'], data['lastName'], data['phoneNumber'], data['email']
     #               , data['city'], data['Bio'], data['links'])
    return redirect(url_for('user_views.getSignupPage2',data1=data1))

@user_views.route('/signupPage2<data1>', methods=['GET'])
def getSignupPage2(data1):
    pass
    #return render_template(data1=data1)

@user_views.route('/add_User_Page2<data1>',methods=['POST'])
def create_user_page2(data1):
    data2=request.form
    user=get_user_by_username(data['username'])
    if user:
        flash("Username is taken please enter a new username.")
        #return jsonify("Username is taken please enter a new username.")
    user=create_user(data1['username'], data1['password'], data1['firstName'], data1['lastName'], data2['phoneNumber'], data1['email']
                    , data2['city'], data2['Bio'], data2['links'])
    return jsonify(user)

@user_views.route('/login',methods=['POST'])
def loginUser():
    data=request.form
    permittedUser=authenticate(data['username'], data['password'])
    if permittedUser==None:
        flash("Wrong Credentials, Please try again")
        #return redirect(url_for(''))
    login_user(permittedUser,remember=True)
    flash('You were successfully logged in!')
    pass
    #return redirect(url_for(''))






@user_views.route('/getAllUsers', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return jsonify(users)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))
    


#@user_views.route('/identify', methods=['GET'])
#@jwt_required()
#def identify_user_action():
#    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

#@user_views.route('/static/users', methods=['GET'])
#def static_user_page():
#  return send_from_directory('static', 'static-user.html')