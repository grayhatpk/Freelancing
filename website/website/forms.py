from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , IntegerField , SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class register(FlaskForm):
    username = StringField(label='Username: ' , validators=[Length(min=2 , max=20) , DataRequired() ])
    email = StringField(label='Email:' , validators=[ Email() , DataRequired() ])
    password1 = PasswordField(label="Password: ", validators=[Length(min=6) , DataRequired()])
    password2 = PasswordField(label='Confirm Password: ' , validators=[ EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register!')
    
    
class login(FlaskForm):
    username = StringField(label='Username: ' , validators= [ DataRequired() ] )
    password  = PasswordField(label='Password: ' , validators=[ DataRequired()])
    submit = SubmitField(label='Login!')

