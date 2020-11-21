import requests
import json
import random


def get_quote():
    r = requests.get("https://type.fit/api/quotes")
    json_data = json.loads(r.text)
    random_quote = random.choice(json_data)

    tg_format = random_quote['text']+'\n'+random_quote['author']
    return tg_format 

