from flask import Blueprint

auth = Blueprint('auth',__name__)
#Adrian: I shortened the authenticate to auth 

from . import views