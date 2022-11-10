#Импорты
from thefuzz import fuzz
from thefuzz import process
import torch
import sounddevice as sd
import time

#основные (статичные) переменные
names = ["саша", "саня", "александр"]
times = ["сколько время?", "который час?", "сколько времени"]
translate = ["переведи", "перевод"]

#Модель голоса
language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
device = torch.device('cpu') # gpu or cpu

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                    model='silero_tts',
                                    language=language,
                                    speaker=model_id)
model.to(device)


def play (text: str): #Воспроизведение звука
    audio = model.apply_tts(text=text,
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=True,
                            put_yo=True)

    sd.play(audio, sample_rate * 1.05) #Воспроизводим
    time.sleep((len(audio) / sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
    sd.stop() #Останавливает воспроизведение

#На выходе должен выдовать стринговую переменную, для дальнейшего использования
def input ():
    text = str(input())
    text = text.lower()
    return text

def name_removing (text):
    text = input ()
    for i in range(len(names)):
        if text.startswith(names[i]):
            text = text.replace(names[1], "")
            return text


#Главная логика (распределение задач по функциям)
def processing ():
    for x in range(len(times)):
        pass

def cmd (text):
    pass