import speech_recognition as sr
from translate import Translator
from .member import Member
from bs4 import BeautifulSoup
import requests
import json

r = sr.Recognizer()

__all__ = ("Recognition", "Wikipedia", "Translate", 'Geo')





class Recognition:
    def start():
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(source=mic)

    def recognition():
        try:
            with sr.Microphone() as mic:
                audio = r.listen(source=mic)
                recogn = r.recognize_google(audio_data=audio, language='ru-RU')
                return str(recogn)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass

class Wikipedia:
    def search(self, page: str):
        response = requests.get(
            url=f"https://en.wikipedia.org/wiki/{page}",
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="firstHeading")
        return title.string




class Translate:

    def translator_en (text:str):
        translator_eng = Translator(from_lang='en', to_lang='ru')
        end_text = translator_eng.translate(text)
        return end_text

    def translator_ru (text:str):
        translator_rus = Translator(from_lang='ru', to_lang= 'en')
        end_text = translator_rus.translate(text)
        return end_text

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
    

class Intents:
    recognition = Recognition()
    
    wiki = Wikipedia()

    translate = Translate()

    geo = Geo()

    member = Member()



