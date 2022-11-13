#Импорты
from thefuzz import fuzz
from thefuzz import process
import sounddevice as sd
#import speech_recognition as sr
import torch
import time


#основные (статичные) переменные
names = ["саша", "саня", "александр", "санёк"]
times = ["сколько время", "который час", "сколько времени"]
translate = ["переведи", "перевод"]
weather = ["какая погода", "что одеть на улицу", "какая температура", "сколько градусов"]



#Модель голоса
language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
device = torch.device('cpu') # gpu or cpu
#recognizer = sr.Recognizer()


model, null = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                    model='silero_tts',
                                    language=language,
                                    speaker=model_id)
model.to(device)


def speech_recognition():
    pass

def play(text: str):
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=True,
                            put_yo=True)

    sd.play(audio, sample_rate * 1.05) #Воспроизводим
    time.sleep((len(audio) / sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
    sd.stop() #Останавливает воспроизведение
    print(text)


#На выходе должен выдовать стринговую переменную, для дальнейшего использования
def input_i():
    text = input()
    text = text.lower()
    return text

#Главная логика (распределение задач по функциям)
def recognize(text):
    text = input_i()
    for i in range(len(names)):
        if text.startswith(names[i]):
            text = text.replace(names[1], "")
            return text


#Главная логика (распределение задач по функциям)

def processing ():
    text = recognize(input_i())

    #time
    now_t = 0
    max_t = 0 #максимальные совпадения по категории времени
    for x in range(len(times)):
        now_t = fuzz.ratio(text, times[x]) #сравнение
        if now_t > max_t:
            max_t = now_t
        if max_t < 60:
            max_t = 0 
    
    #translate
    now_tr = 0
    max_tr = 0 #максимальные совпадения по категории перевода
    for z in range(len(translate)):
        now_tr = fuzz.ratio(text, translate[z]) #сравнение
        if now_tr > max_tr:
            max_tr = now_tr
        if max_tr < 60:
            max_tr = 0

    #weather
    now_w = 0
    max_w = 0 #максимальные совпадения по категории погоды
    for p in range(len(translate)):
        now_w = fuzz.ratio(text, weather[p]) #сравнение
        if now_w > max_w:
            max_w = now_w
        if max_w < 60:
            max_w = 0

    #вывод
    if max_t > max_tr:
        time_f()
    elif max_tr > max_t:
        translate_f()
    elif max_w > max_t & max_tr:
        weather_f()
    else:
        play ("Вы хотите поговорить")

#commands
def time_f():
    pass

def translate_f():
    pass

def weather_f():
    pass

while True:
    processing()