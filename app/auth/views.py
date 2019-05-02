from flask import render_template,redirect,url_for, flash,request
from . import auth
from flask_login import login_user,logout_user,login_required, current_user
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db


@auth.route('/register' ,methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        admin = Admin(first_name = form.first_name.data,
                    last_name = form.last_name.data,
                    email = form.email.data, 
                    username = form.username.data,
                    password = form.password.data)
        db.session.add(admin)
        db.session.commit()
        # Add email functionality in future may be?
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html', form = form)

@auth.route('/login')    
def login():

    return render_template('auth/login.html')

@auth.route('/logout')    
def logout():
    return render_template('admin/welcome.html')