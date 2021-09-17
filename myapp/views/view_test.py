from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
from read import ReadFile

test_blueprint = Blueprint('test_blueprint', __name__, template_folder='templates', static_folder='static')

@test_blueprint.route('/test')
def test():
    try:
        log = ReadFile.leitura_arquivo()
        return render_template("test.html", log = log)
    except TemplateNotFound:
        abort(404)

@test_blueprint.route('/buttonback', methods=["POST"])
def buttonback():
    try:
        return redirect('/index')
    except TemplateNotFound:
        abort(404)