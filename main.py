#Импорты
from pyowm import OWM 
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from api import num2text as n2t
from api import recognize as rc
from api import db
from api import geo
from thefuzz import fuzz
from thefuzz import process
import sounddevice as sd
from translate import Translator
import torch
import time
import datetime



#основные (статичные) переменные
config_dict = get_default_config()
config_dict['language'] = 'ru'
names = ["саша", "саня", "александр", "санёк"]
times = ["сколько время", "который час", "сколько времени"]
translate_list = ["переведи", "перевод", "перевод слова"]
translated = ["переведи диалог", "перевод диалога", "функция диалогового перевода", "функция перевода диалога"]
weather = ["какая погода", "что одеть на улицу", "какая температура", "сколько градусов"]
al_clock = ["поставь будильник", "будильник", "новый будильник"]



#Модель голоса
language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
device = torch.device('cpu') # gpu or cpu
translate = Translator(from_lang="en", to_lang="ru")
clock = db.AlarmClock()

model, null = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                    model='silero_tts',
                                    language=language,
                                    speaker=model_id)
model.to(device)


def speech_recognition():
    pass

def play(text: str):
    print("- " + text)
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=True,
                            put_yo=True)

    sd.play(audio, sample_rate * 1.05) #Воспроизводим
    time.sleep((len(audio) / sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
    sd.stop() #Останавливает воспроизведение


#На выходе должен выдовать стринговую переменную, для дальнейшего использования
def input_i():
    text = str(rc.recognition())
    text = text.lower()
    return str(text)


def startingwithname():
    text = input_i()
    for i in range(len(names)):
            if text.startswith(str(names[i])):
                print("- " + text)
                text = text.replace(names[i], '')
                processing(text)
                


#Главная логика (распределение задач по функциям)
def processing(text):
    #time
    now_t = 0
    max_t = 0 #максимальные совпадения по категории времени
    for x in range(len(times)):
        now_t = fuzz.ratio(text, times[x]) #сравнение
        if now_t > max_t:
            max_t = now_t
        if max_t < 60:
            max_t = 0 
    
    #weather
    now_trd = 0
    max_trd = 0 #максимальные совпадения по категории погоды
    for u in range(len(translated)):
        now_trd = fuzz.ratio(text, translated[u]) #сравнение
        if now_trd > max_trd:
            max_trd = now_trd
        if max_trd < 60:
            max_trd = 0

    #translate
    now_tr = 0
    max_tr = 0 #максимальные совпадения по категории перевода
    for z in range(len(translate_list)):
        now_tr = fuzz.ratio(text, translate_list[z]) #сравнение
        if now_tr > max_tr:
            max_tr = now_tr
        if max_tr < 60:
            max_tr = 0

        #weather
    now_w = 0
    max_w = 0 #максимальные совпадения по категории погоды
    for p in range(len(weather)):
        now_w = fuzz.ratio(text, weather[p]) #сравнение
        if now_w > max_w:
            max_w = now_w
        if max_w < 60:
            max_w = 0
    
    
    
    #alarm clock
    now_al = 0
    max_al = 0 #максимальные совпадения по категории перевода
    for a in range(len(al_clock)):
        now_al = fuzz.ratio(text, al_clock[a]) #сравнение
        if now_al > max_al:
            max_al = now_al
        if max_al < 60:
            max_al = 0

    #вывод
    if max_t > max_tr:
        time_f()
    elif max_tr > max_t:
        translate_f(text)
    elif max_w > max_t & max_tr:
        weather_f()
    elif max_trd > max_t & max_tr & max_w:
        translate_df()
    elif max_al > max_trd & max_t & max_tr & max_w:
        add_alarm_clock(text)
    else:
        play("Вы хотите поговорить?")


#commands
def time_f():
    now = datetime.datetime.now()
    text = f"Сейчас {n2t.int_to_ru(now.hour)} {n2t.int_to_ru(now.minute)}"
    play(text)

def translate_f(text: str):
    for i in range(len(translate_list)):
        text = text.replace(translate_list[i], '')
    tr = translate.translate(text)
    play(tr)

def translate_df():
    play("Извините, но данная функция не доступна. Попробуйте обновить клиент и повторить попытку позже!")

def weather_f():
    city = str(geo.getcity())
    country_code = str(geo.getcountry())
    merge = city + ',' + country_code
    play ("This function doesn't exist")

def add_alarm_clock(text: str):
    for i in range(len(al_clock)):
        time = text.replace(al_clock[i], '')
    clock.add("School", 1664200798) #создаём будильник 
    play("Будильник добавлен")

def parse_clock_names():
    l = clock.get_clocks() 
    for i in l:
        print(i[0])

print("Sanya 2.0 in using")
rc.start()

while True:
    startingwithname()
