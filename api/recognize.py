import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
def start():
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(source=mic)

def recognition(language = 'ru-RU'):
    try:

        with sr.Microphone() as mic:
            audio = r.listen(source=mic)
            recogn = r.recognize_google(audio_data=audio, language=language)
            return(str(recogn))
            
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass