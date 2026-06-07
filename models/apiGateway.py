import os
import requests
from dotenv import load_dotenv, dotenv_values 


load_dotenv() 
URL=os.getenv("AI_URL")


async def get_response(body=""):
    url=f"{URL}/{body}"
    respons=requests.get(url)
    if respons.status_code == 200:
        data = respons.json()
        try:
            print("trying")
        except AttributeError or data is None:
            print("error")

