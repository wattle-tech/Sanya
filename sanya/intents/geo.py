import requests
import json

__all__ = ("Geo")

class Geo(): 

    @property
    def city(self) -> str:
        url = 'https://ipinfo.io/json'
        res = requests.get(url).text
        data = json.loads(res)
        return data['city']
        
    @property
    def country(self) -> str:
        url = 'https://ipinfo.io/json'
        res = requests.get(url).text
        data = json.loads(res)
        return data['country']