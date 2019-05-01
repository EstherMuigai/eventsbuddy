# app/models.py
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin, LoginManager
from datetime import datetime
from flask_login import UserMixin


class Admin(UserMixin,db.Model):
    '''
    class for users
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



class Event(db.Model):
    __tablename__ = "events"
    '''
    Class for events
    '''
    # Relationship with the admin table
    admin = db.relationship(Admin)
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable = False)
    event_date = db.Column(db.DateTime, index=True, nullable = False)

    # Relationship with the question table 
    question = db.relationship('Question',backref = 'events', nullable = False)
    
    def __init__(self,timestamp, title, body, event_date,user_id):
        self.title = title
        self.body = body
        self.event_date = event_date
        self.event_id = event_id
        self.user_id = user_id

    def generate_events_id():
        pass
        
    def __repr__(self):
        return f"EVENT ID:{self.id} -- Date: {self.timestamp}"    


class Question(db.Model):
    __tablename__ = "questions"
    '''
    Class for Questions
    '''
    # Relationship with the events table
    events = db.relationship(Event)
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(120), nullable=False)
    # This is auto-generated and links the event to future user sessions.
    event_id = db.Column(db.String(8), nullable = False)
    # Relationship with the questions for the event
    responses = db.relationship('Answer', backref = 'questions', lazy = "dynamic")
    
    def __init__(self,body, event_id):
        self.body =body
        self.event_id = event_id
    
    def __repr__(self):
        return f"Question:{self.body} -- Event: {self.event_id}"    

class Response(db.Model):
    __tablename__ = "responses"
    '''
    Class for Responses
    '''
    # Relationship with the questions table
    questions = db.relationship(Question)

    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    body = db.Column(db.Text, nullable = False)
    # Relationship with the questions for the event
    users = db.relationship('User', backref = 'questions', lazy = "dynamic")
    
    def __init__(self,question,timestamp,title, body, users):
        self.question = question
        self.timestamp = timestamp
        self.body = body
        self.users = users
   
    def __repr__(self):
        return f"Question :{self.question} -- Response: {self.body}"    


class User(db.Model):
    __tablename__ = "users"
    '''
    Class for users
    '''
    # Relationship with the Responses table
    responses = db.relationship(Response)
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    device_id = db.Column(db.Text, nullable = False)

    def __init__(self,question_id, device_id,body, user_id):
        self.question_id = question_id
        self.device_id - device_id
        self.user_id = user_id

        
    def __repr__(self):
        return f"USER ID:{self.device_id}----Respons ID:{self.question_id}"    