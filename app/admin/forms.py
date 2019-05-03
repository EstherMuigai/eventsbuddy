from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length

class QuestionForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired(), Length(min=10, max=120)])
    Publish = SubmitField('Publish')

class DeleteQuestion(FlaskForm):
    content_id = StringField('')
    Delete = SubmitField('Delete')

class AnswerQuestion(FlaskForm):
    answer = StringField('Answer', validators=[DataRequired(), Length(min=1, max=120)])
    Send = SubmitField('Publish')

class CreateEvent(FlaskForm):
    title = StringField('Event Name', validators=[DataRequired(), Length(min=5, max=50)])
    body = StringField('Description', validators=[DataRequired(), Length(min=10, max=250)])
    event_date = DateTimeField('On', validators=[DataRequired()])
    publish = SubmitField('Create Event')