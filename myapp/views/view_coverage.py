from flask import Blueprint, render_template, abort, request, redirect
from jinja2 import TemplateNotFound
import os


template_dir = os.path.abspath('htmlcov')
coverage_blueprint = Blueprint('coverage_blueprint', __name__, template_folder=template_dir)

@coverage_blueprint.route('/coverage')
def coverage():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        abort(404)

@coverage_blueprint.route('/buttonback', methods=["POST"])
def buttonback():
    try:
        return redirect('/index')
    except TemplateNotFound:
        abort(404)


