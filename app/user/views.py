from flask import render_template,redirect,url_for
from .forms import EventCodeForm
from . import user
from datetime import datetime
from ..models import User, Event, Question

@user.route('/',methods=['GET','POST'])
def user_screen():
    '''
    This function handles user authentication/ ghost-registration.
    it checks if the event he/she wants to join is in session before rendering the event page if it exists
    '''
    code = EventCodeForm()
    events = Event.query.all()
    if EventCodeForm.validate_on_submit():
        invite_code = EventCodeForm.code.data
        if invite_code in events.event_id:
            new_user = User('0',datetime.utcnow().strftime("%H:%M"),invite_code)
        
            return redirect(url_for('user.event_view', current_user = new_user ))
    return render_template('user/user-screen.html', code = code )


@user.route('/profile/<id>')
def event_view(id):
    code = EventCodeForm()
    if code.validate_on_submit():
        return redirect(url_for('user.event_view'))
    return render_template('user/user-event.html',code=code)