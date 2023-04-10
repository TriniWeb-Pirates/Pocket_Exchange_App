import os
from flask import Flask
from flask_login import LoginManager, current_user, login_manager
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta
from App.models import User, LendingOffer,LendingRequest


from App.database import create_db, get_migrate

from App.controllers import (
    setup_jwt
)

from App.views import views


def add_views(app):
    for view in views:
        app.register_blueprint(view)


def loadConfig(app, config):
    app.config['ENV'] = os.environ.get('ENV', 'DEVELOPMENT')
    delta = 7
    if app.config['ENV'] == "DEVELOPMENT":
        app.config.from_object('App.config')
        #delta = app.config['JWT_EXPIRATION_DELTA']
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        app.config['DEBUG'] = os.environ.get('ENV').upper() != 'PRODUCTION'
        app.config['ENV'] = os.environ.get('ENV')
        #delta = os.environ.get('JWT_EXPIRATION_DELTA', 7)
        
    #app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=int(delta))
        
    for key, value in config.items():
        app.config[key] = config[key]

def create_app(config={}):
    app = Flask(__name__, static_url_path='/static')
    CORS(app)
    loadConfig(app, config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEVER_NAME'] = '0.0.0.0'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    create_db(app)
    login_manager=LoginManager(app)#added login manager 
    login_manager.init_app(app)#pass app to login manager
    migrate=get_migrate(app)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    #setup_jwt(app)
    app.app_context().push()
    return app

app=create_app()
app=Flask(__name__)
login_manager=LoginManager(app)#added login manager 
login_manager.init_app(app)#pass app to login manager
#login_manager.login_view = 'user_views'
migrate=get_migrate(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)