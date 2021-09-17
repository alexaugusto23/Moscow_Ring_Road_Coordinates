from flask import Blueprint, render_template, abort, request, templating
from jinja2 import TemplateNotFound
from dotenv import load_dotenv
from manager import ManagerFile
import requests
import os
import json

from werkzeug.utils import redirect

load_dotenv()

API_KEY = os.environ.get('API_KEY')


index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates', static_folder='static')

@index_blueprint.route('/')
@index_blueprint.route('/index')
def index() -> templating:
    # Route to render template.
    try:
        return render_template('index_mkad.html')
    except TemplateNotFound:
        abort(404)

@index_blueprint.route("/form", methods=["PUT", "POST"])
def form(origin: str = None, destiny: str = None ) -> str:
    # Function to make a request to google maps.
   
    origin = request.form['origin']
    destiny = request.form['destiny']
    print(f"Origin:{origin}/nDestiny:{destiny}")

    origins = origin
    destinations = destiny

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={API_KEY}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    maps = json.loads(response.text)
    if maps['status'].lower() == 'ok':
        distancia = str(maps['rows'][0]['elements'][0]['distance']['text'])
        return render_template('index.html',distancia=distancia) 
    else:
        return 'Not found'

@index_blueprint.route("/buttontest", methods=["PUT", "POST"])
def buttontest() -> templating:
    ManagerFile.deleta_cria_file()
    return redirect('test')

@index_blueprint.route("/buttoncover", methods=["PUT", "POST"])
def buttoncover() -> templating:
    os.system('coverage run -m unittest discover')
    os.system('coverage html')
    return redirect('coverage')
