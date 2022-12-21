from .intents import recognition
import sounddevice as sd
import torch
import time

__all__ =(
    "Assistant"
)

class Assistant:
    def __init__(self) -> None:
        self.__model = 0
        self.__sample_rate = 48000
        self.__noise = 0

    
    def __en_voice(self, text: str):
        #Модель голоса на английском
        global model_en
        language_en = 'en'
        model_id_en = 'v3_en'
        speaker_en = 'en_1'
        device_en = torch.device('cpu') # gpu or cpu
        if self.__model == 0:
            model_en, null = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                model='silero_tts',
                                                language=language_en,
                                                speaker=model_id_en)
            model_en.to(device_en)
            self.__model += 1
        audio_en = model_en.apply_tts(text=text,
                                    speaker=speaker_en,
                                    sample_rate=self.__sample_rate,
                                    put_accent=True,
                                    put_yo=True)
        sd.play(audio_en, self.__sample_rate * 1.05) #Воспроизводим
        time.sleep((len(audio_en) / self.__sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
        sd.stop() #Останавливает воспроизведение
        

    def __ru_voice(self, text: str):
        #Модель голоса
        global model
        language = 'ru'
        model_id = 'v3_1_ru'
        speaker = 'eugene' #aidar, baya, kseniya, xenia, eugene, random
        device = torch.device('cpu') # gpu or cpu

        if self.__model == 0:
            model, null = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                model='silero_tts',
                                                language=language,
                                                speaker=model_id)
            model.to(device)
            self.__model += 1
        audio = model.apply_tts(text=text,
                                speaker=speaker,
                                sample_rate=self.__sample_rate,
                                put_accent=True,
                                put_yo=True)
        sd.play(audio, self.__sample_rate * 1.05) #Воспроизводим
        time.sleep((len(audio) / self.__sample_rate) + 0.5) #Ждёт столько сколько, идёт аудио
        sd.stop()
    

    def say(self, text: str):
        """:meth:`.say` is use for playing some text"""
        lang = "ru"

        if lang == "en":
            self.__en_voice(text)
            
        if lang == "ru":
            self.__ru_voice(text)
        else:
            raise ValueError("This language isn't supported!")
    

    def listen(self):
        if self.__noise == 0:
            recognition.start()
            self.__noise += 1
        else:
            return str(recognition.listen())
    


    