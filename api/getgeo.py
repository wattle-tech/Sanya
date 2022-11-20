from urllib.request import urlopen
from json import load

def getcity():
    url = 'https://ipinfo.io/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    #will print the data line by line
    print(data['city'])

def getcountry():
    url = 'https://ipinfo.io/json'
    res = urlopen(url)
    #response from url(if res==None then check connection)
    data = load(res)
    #will load the json response into data
    #will print the data line by line
    print(data['country'])

getcity()
getcountry()