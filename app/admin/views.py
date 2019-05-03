from flask import render_template, redirect, url_for
from . import admin
from datetime import datetime, date
from..models import Event, Admin, Question, Response, User
from .. import db
from .forms import QuestionForm, AnswerQuestion, DeleteQuestion, CreateEvent

@admin.route('/')
def admin_welcome():

    return render_template('admin/welcome.html')




@admin.route('/dashboard/<int:id>')    
def dashboard(id):
    title = 'Dashboard'
    administrator = Admin.query.filter_by( id = id ).first()
    events = Event.query.filter_by( admins = id ).all()
    create_event = CreateEvent()


    if CreateEvent.validate_on_submit():
        title = 'Create Event'
        data = CreateEvent()
        new_event = Event( data.event_date.data,
            data.title.data, data.body.data, data.event_date.data, administrator.id
        )
        new_event.save_event(new_event)
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/dashboard.html', title = title, administrator = administrator, admins_events = events, form = create_event )








@admin.route('/event_page/<id>')    
def event_page(id):
    '''
    this function returns the event page, displaying its' details, questions, and answers.
    it also allows rendering of the question form on the fly onto it
    '''
    event = Event.query.filter_by(id = id).first() #gets the event by id
    title = f'Event {event.title}' #passes the event title
    event_questions = Question.query.filter_by(events = id).all() #returns all questions filtered by the session id.
    all_answers = Response.query.all() # returns all answers but not sorted.
    delete_question = DeleteQuestion()

    if QuestionForm.validate_on_submit():
        form = QuestionForm()
        new_question = Question( form.question.data, id )
        new_question.save_question(new_question)
        return redirect(url_for('admin.event_page'))
        
    return render_template('admin/event_page.html', event = event, title = title, event_questions = event_questions, answers = all_answers, delelteQuestion = delete_question)

