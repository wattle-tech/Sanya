from urllib.request import urlopen
from json import load

def get_city() -> str:
    url = 'https://ipinfo.io/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    return data['city']
    #will load the json response into data
    #will print the data line by line

def get_country() -> str:
    url = 'https://ipinfo.io/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    return data['country']
    #will load the json response into data
    #will print the data line by line


