from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
#from flask_jwt import jwt_required, current_identity

from.index import index_views

from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/add_User',methods=['POST'])
def create_user():
    data=request.form
    user=get_user_by_username(data['username'])
    if user:
        flash("Username is taken please enter a new username.")
        #return jsonify("Username is taken please enter a new username.")
    user=create_user(data['username'], data['password'])
    pass
    #return render_template("login.html")

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






@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

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