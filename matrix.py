import requests
import os 
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

# origins='-23.5353749,-46.7625787'
# destinations='48.8589507,2.2770197'

# origins='avmanoelpedropimentel,101'
# destinations='ruamargarida,26'

origins = '55.790847,37.1547731'
destinations = '52.8935659,29.9569978'

regions = None

url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={API_KEY}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

maps = json.loads(response.text)
print(maps['rows'][0]['elements'][0]['distance']['text'])