from flask import render_template,redirect,url_for
from .forms import EventCodeForm
from . import user

@user.route('/',methods=['GET','POST'])
def user_screen():
    code = EventCodeForm()
    if code.validate_on_submit():
        return redirect(url_for('user.event_view'))
    return render_template('user/user-screen.html',code=code)

@user.route('/profile')
def event_view():
    code = EventCodeForm()
    if code.validate_on_submit():
        return redirect(url_for('user.event_view'))
    return render_template('user/user-event.html',code=code)