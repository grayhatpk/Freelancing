from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager , current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db_name = 'website.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db' #main line for the connection 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "379aa8c95f215772a5ed34e1"    # For Security Purposes 

db = SQLAlchemy(app) # an app for the database 

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category  = 'info'
bcrypt =Bcrypt(app)
@login_manager.user_loader
def load_user(user_id):
    return current_user.get(user_id)

from website import routes, models