from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index_blueprint = Blueprint('index_blueprint', __name__)

@index_blueprint.route('/')
@index_blueprint.route('/index/')
def index():
    try:
        return '<h1>This is flask blueprint example</h1>'
    except TemplateNotFound:
        abort(404)