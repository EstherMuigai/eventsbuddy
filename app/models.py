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
    profile_image = db.Column(db.String, nullable = False, default = 'default_profile_image.png')
    email = db.Column(db.String(100), unique = True, index =True)
    username = db.Column(db.String(72), unique=True,index=True)
    password_hash = db.Column(db.String(255))

    # Relationship with the Blog Post
    events = db.relationship('Event', backref = 'author', lazy = "dynamic")

    def __init__(self,email, username, password):
        self.email = email
        self.username =  username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
        
    def __repr__(self):
        return f"User {self.username}"



class Event(db.Model):
    __tablename__ = "events"
    '''
    Class for events
    '''
    # Relationship with the question table
    users = db.relationship(Question)

    id = db.Column(db.Integer, primary_key = True)
    # Relationship with the admin table 
    admin_id = db.Column(db.Integer,db.ForeignKey('admins.id'), nullable = False)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable = False)
    event_date = db.Column(db.DateTime, index=True, nullable = False)
    # Relationship with the questions for the event
    admin = db.relationship('Admin', backref = 'events', lazy = "dynamic")
    
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
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key = True)
    # Relationship with the admin table 
    admin_id = db.Column(db.Integer,db.ForeignKey('admins.id'), nullable = False)
    title = db.Column(db.String(120), nullable=False)
    # This is auto-generated and links the event to future user sessions.
    event_id = db.Column(db.String(8), nullable = False)
    
    # Relationship with the questions for the event
    questins = db.relationship('Question', backref = 'event', lazy = "dynamic")
    
    def __init__(self,title,user_id, event_id):
        self.admin_id = admin_id
        self.title =title
        self.user_id = user_id
        self.event_id = event_id


        
    def __repr__(self):
        return f"Question:{self.title} -- Admin: {self.admin_id}--Event:{self.event_id}"    



class Response(db.Model):
    __tablename__ = "responses"
    '''
    Class for Responses
    '''
    # Relationship with the events table
    users = db.relationship(User)

    id = db.Column(db.Integer, primary_key = True)
    # Relationship with the admin table 
    question_id = db.Column(db.Integer,db.ForeignKey('admins.id'), nullable = False)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    body = db.Column(db.Text, nullable = False)
    # This is auto-generated and links the event to future user sessions.
    event_id = db.Column(db.String(8), nullable = False)
    
    # Relationship with the questions for the event
    questins = db.relationship('Question', backref = 'event', lazy = "dynamic")
    
    def __init__(self,title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id

    def generate_events_id():
        pass


        
    def __repr__(self):
        return f"EVENT ID:{self.id} -- Date: {self.timestamp}"    





class Users(db.Model):
    __tablename__ = "users"
    '''
    Class for users
    '''
    # Relationship with the events table
    questions = db.relationship(Question)

    id = db.Column(db.Integer, primary_key = True)
    # Relationship with the admin table 
    question_id = db.Column(db.Integer,db.ForeignKey('admins.id'), nullable = False)
    timestamp = db.Column(db.DateTime, index=True, nullable = False, default=datetime.utcnow)
    device_id = db.Column(db.Text, nullable = False)

    
    # Relationship with the questions for the event
    questins = db.relationship('Question', backref = 'event', lazy = "dynamic")
    
    def __init__(self,question_id, device_id,body, user_id):
        self.question_id = question_id
        self.device_id - device_id
        self.user_id = user_id

    def generate_device_id():
        pass


        
    def __repr__(self):
        return f"USER ID:{self.device_id}"    