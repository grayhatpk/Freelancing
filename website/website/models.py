from website import db , login_manager , bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    id  = db.Column(db.Integer(), primary_key=True ,nullable= False , unique=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True)
    email = db.Column(db.String(), nullable= False , unique=True)
    password_hash  = db.Column(db.String(), nullable= False)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash  = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash , attempted_password)
