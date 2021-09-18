import re 
import requests

r = requests.get('http://127.0.0.1:5000/')
r = requests.post('http://127.0.0.1:5000/form',data={'origin':'55.790847,37.1547731', 'destiny':'52.8935659,29.9569978'})

string ='646 km'

text = r.text.split(' ')
print(text)

# padrao = "([0-9]{0,1000000000}) ([a-z]{2})"
# # resposta = re.findall(padrao, string)
# resposta = re.search(padrao, string).group()
# print(resposta)

