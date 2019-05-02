from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from ..models import User


class RegistrationForm(FlaskForm):
    
    first_name = StringField('First Name:', validators = [Required())
    first_name = StringField('First Name:', validators = [Required())
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Register')
    
    
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')
      
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')