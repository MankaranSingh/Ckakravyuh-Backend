from flask import render_template
from . import error

@error.app_errorhandler(404)
def page_not_found(e):
    return 'Yahaan kaise aana hua ?'
