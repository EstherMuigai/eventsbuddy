from flask import render_template
from . import user

@user.route('/')
def test_user():
    return render_template('user/test_user.html')