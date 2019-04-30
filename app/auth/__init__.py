from flask import Blueprint

auth = Blueprint('authenticate',__name__)

from . import views