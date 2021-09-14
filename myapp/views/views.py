from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

API_KEY = os.environ.get('API_KEY')

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates', static_folder='static')

@index_blueprint.route('/')
@index_blueprint.route('/index/')
def index():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@index_blueprint.route("/form", methods=["PUT", "POST"])
def form():
   
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


    




