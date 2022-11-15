import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

try:
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(source=mic)
        audio = r.listen(source=mic)
        recogn = r.recognize_google(audio_data=audio, language='ru-RU')
except sr.UnknownValueError:
    pass
except sr.RequestError:
    pass

print (str(recogn))