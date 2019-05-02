from flask import render_template
from . import admin

@admin.route('/')
def admin_welcome():
    return render_template('admin/welcome.html')

@admin.route('/dashboard')    
def dashboard():
    return render_template('admin/dashboard.html')

@admin.route('/create_event')    
def create_event():
    return render_template('admin/create_event.html')

@admin.route('/event_page')    
def event_page():
    return render_template('admin/event_page.html')

@admin.route('/create_question')    
def create_question():
    return render_template('admin/create_question.html')