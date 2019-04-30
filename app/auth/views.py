from flask import render_template
from . import auth

@auth.route('/')
def test_auth():
    return render_template('auth/test_auth.html')