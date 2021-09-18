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

# origins = '37.842789,55.76522'
# destinations = '70.0464,108.4749'

origins = ' 56.8465,35.8627'
destinations = '57.0175,35.9605'
    


regions = None

url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={API_KEY}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

maps = json.loads(response.text)
print(maps)
print(maps['rows'][0]['elements'][0]['status'])
# print(maps['rows'][0]['elements'][0]['distance']['text'])