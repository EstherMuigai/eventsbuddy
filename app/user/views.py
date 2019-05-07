from flask import render_template,redirect,url_for
from .forms import EventCodeForm, AnswerQuestion
from . import user
from datetime import datetime
from ..models import User, Event, Question

@user.route('/',methods=['GET','POST'])
def user_screen():
    '''
    This function handles user authentication/ ghost-registration.
    it checks if the event he/she wants to join is in session before rendering the event page if it exists
    '''
    code_form = EventCodeForm()

    if code_form.validate_on_submit():
        event_code = Event.query.filter_by(event_id = code_form.input_code.data).first()
        if event_code:
            questions = Question.query.filter_by(event = event_code).all()
            

            return redirect(url_for('user.event_view{}'.format(event_code), questions = questions))



    # events = Event.query.all()
    # if code.validate_on_submit():
    #     invite_code = code.input_code.data
    #     if invite_code in events.event_id:
    #         new_user = User('0',datetime.utcnow().strftime("%H:%M"),invite_code)
        
    #         return redirect(url_for('user.event_view', current_user = new_user ))
    return render_template('user/user-screen.html', code = code_form )


@user.route('/profile/<id>')
def event_view(id):
    question_form = que
    if code.validate_on_submit():
        return redirect(url_for('user.event_view'))
    return render_template('user/user-event.html',code=code)