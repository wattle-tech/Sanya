import requests
import json

def get_city() -> str:
    url = 'https://ipinfo.io/json'
    res = requests.get(url).text
    #response from url(if res==None then check connection)
    data = json.loads(res)
    return data['city']
    #will load the json response into data
    #will print the data line by line

def get_country() -> str:
    url = 'https://ipinfo.io/json'
    res = requests.get(url).text
    #response from url(if res==None then check connection)
    data = json.loads(res)
    return data['country']
    #will load the json response into data
    #will print the data line by line