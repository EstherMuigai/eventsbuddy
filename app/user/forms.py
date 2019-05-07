from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Required, Length
from wtforms import SubmitField,StringField

class EventCodeForm (FlaskForm):
    input_code = StringField( 'Enter Invitation Code.',validators = [Required()])
    submit = SubmitField( 'Submit', validators = [Required()])

class AnswerQuestion(FlaskForm):
    answer = StringField('Answer', validators=[DataRequired(), Length(min=1, max=120)])
    Send = SubmitField('Publish')