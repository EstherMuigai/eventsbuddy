from flask import render_template
from . import admin

@admin.route('/')
def test_admin():
    return render_template('admin/test_admin.html')