import requests
import os 
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

# origins='-23.5353749,-46.7625787'
# destinations='48.8589507,2.2770197'

# origins='avmanoelpedropimentel,101'
# destinations='ruamargarida,26'

origins = '-23.5353749,-46.7625787'
destinations = '29.7147592,-95.4324201'

regions = ['.br','.ru','.us']

url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins}&destinations={destinations}&key={API_KEY}&region={regions}"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)