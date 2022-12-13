from .client import *
from .recognize import Recognition
import sounddevice as sd
import torch
import time

__all__ =(
    "Assistant"
)

class Assistant(Client):
    def __init__(self) -> None:
        self.sample_rate = 48000
        self.noise = 0
        

    def _en_model(self, text: str):
        #Модель голоса на английском
        language_en = 'en'
        model_id_en = 'v3_en'
        speaker_en = 'en_1'
        device_en = torch.device('cpu') # gpu or cpu

        model_en, null_1 = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                            model='silero_tts',
                                            language=language_en,
                                            speaker=model_id_en)
        model_en.to(device_en)

        audio_en = model_en.apply_tts(text=text,
                                    speaker=speaker_en,
                                    sample_rate=self.sample_rate,
                                    put_accent=True,
                                    put_yo=True)
        sd.play(audio_en, self.sample_rate * 1.05) #Воспроизводим
        time.sleep((len(audio_en) / self.sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
        sd.stop() #Останавливает воспроизведение

    def _ru_model(self, text: str):
        #Модель голоса
        language = 'ru'
        model_id = 'v3_1_ru'
        speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
        device = torch.device('cpu') # gpu or cpu

        model, null = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                            model='silero_tts',
                                            language=language,
                                            speaker=model_id)
        model.to(device)

        audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=self.sample_rate,
                                put_accent=True,
                                put_yo=True)
        sd.play(audio, self.sample_rate * 1.05) #Воспроизводим
        time.sleep((len(audio) / self.sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
        sd.stop()
        
    

    def say(self, text: str):
        """:meth:`.say` is use for playing some text"""
        lang = "en"

        if lang == "en":
            self._en_model(text)
        else:
            self._ru_model(text)
    

    def listen(self):
        if self.noise == 0:
            Recognition.start()
            self.noise += 1
        else:
            return Recognition.recognition()
    


    