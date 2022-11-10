#Импорты
from thefuzz import fuzz
from thefuzz import process
import torch
import sounddevice as sd
import time

#основные (статичные) переменные
list = []

#Модель голоса
language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'baya' #aidar, baya, kseniya, xenia, eugene, random
device = torch.device('cpu') # gpu or cpu

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                    model='silero_tts',
                                    language=language,
                                    speaker=model_id)
model.to(device)


def play(text: str):
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

#Главная логика (распределение задач по функциям)
def processing ():
    pass

def cmd (text):
    pass
