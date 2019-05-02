from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import SubmitField,StringField

class EventCodeForm (FlaskForm):
    code = StringField(validators = [Required()])
    submit = SubmitField(validators = [Required()])