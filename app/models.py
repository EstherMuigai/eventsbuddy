# app/models.py
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin, LoginManager
from datetime import datetime
from flask_login import UserMixin
from .get_info import generate_events_id, get_device_id



class Admin(UserMixin,db.Model):
    '''
    class for admins
    '''
    __tablename__='admins'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100), unique = True, index =True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(72), unique=True,index=True)
    password_hash = db.Column(db.String(255))

    # Relationship with the Events Post
    events = db.relationship('Event', backref = 'author', lazy = "dynamic")

    def __init__(self,email, username, first_name,last_name,password):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username =  username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
        
    def __repr__(self):
        return f"Admin {self.first_name}"
    

    def save_admin(self):
        db.session.add(self)
        db.session.commit()


class Event(db.Model):
    __tablename__ = "events"
    '''
    Class for events
    '''
    # Relationship with the admin table
    # admin = db.relationship(Admin)
    admins = db.Column(db.Integer, db.ForeignKey('admins.id'))
    id = db.Column(db.Integer, primary_key = True)
    # timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable = False)
    event_date = db.Column(db.DateTime, index=True, nullable = False)
    event_id = db.Column(db.String(8), nullable = False)

    # Relationship with the question table 
    question = db.relationship('Question',backref = 'events', lazy = "dynamic")
    
    def __init__(self,admins, title, body, event_date, event_id=''):
        self.admins = admins
        self.title = title
        self.body = body
        self.event_date = event_date
        self.event_id = generate_events_id()
 



        
    def __repr__(self):
        return f"EVENT ID:{self.id} -- Date: {self.timestamp}"    
    
    def save_event(self):
        db.session.add(self)
        db.session.commit()

class Question(db.Model):
    __tablename__ = "questions"
    '''
    Class for Questions
    '''
    # Relationship with the events table
    event = db.Column(db.Integer, db.ForeignKey('events.id'))
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(120), nullable=False)
    # This is auto-generated and links the event to future user sessions.
    # Relationship with the questions for the event
    responses = db.relationship('Answer', backref = 'questions', lazy = "dynamic")
    
    def __init__(self,body, event):
        self.body =body
        self.event_id = event
    
    def __repr__(self):
        return f"Question:{self.body} -- Event: {self.event_id}"    

    def save_question(self):
        db.session.add(self)
        db.session.commit()


class Response(db.Model):
    __tablename__ = "responses"
    '''
    Class for Responses
    '''
    # Relationship with the questions table
    questions = db.Column(db.Integer, db.ForeignKey('questions.id'))
    respondent = db.Column(db.Integer, db.ForeignKey('users.id'))

    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    body = db.Column(db.Text, nullable = False)
    
    def __init__(self,respondent,timestamp,questions, body):
        self.questions = questions
        self.respondent = respondent
        self.timestamp = timestamp
        self.body = body
   
    def __repr__(self):
        return f"Question :{self.questions} -- Response: {self.body}"    

    def save_response(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model):
    __tablename__ = "users"
    '''
    Class for users
    '''
    # Relationship with the Responses table
    # responses = db.relationship(Response)
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    device_id = db.Column(db.Text, nullable = False)
    event_code = db.Column(db.Text, nullable = False)
    responses = db.relationship('Response', backref = 'feedback', lazy = 'dynamic')

        

    def __init__(self,device_id, event_code,timestamp):
        self.device_id  = get_device_id()
        self.user_id = user_id
        self.event_code  = event_code
        self.timestamp = timestamp

        
    def __repr__(self):
        return f"USER ID:{self.device_id}----Respons ID:{self.question_id}"    


    def save_user(self):
        db.session.add(self)
        db.session.commit()