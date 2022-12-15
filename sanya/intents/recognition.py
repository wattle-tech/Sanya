import speech_recognition as sr


r = sr.Recognizer()

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