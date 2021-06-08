import requests
import random
import string

token = input("Entrez votre Token: ")
channel_id = input("Entrez l'ID du Salon: ")
headers = {'Authorization': token}

id = ''.join(random.choice(string.digits) for _ in range(1997))
requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': f'<@{id}>'})