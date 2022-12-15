from translate import Translator


__all__ = ("Translate")



class Translate:

    def translator_en (text:str):
        translator_eng = Translator(from_lang='en', to_lang='ru')
        end_text = translator_eng.translate(text)
        return end_text

    def translator_ru (text:str):
        translator_rus = Translator(from_lang='ru', to_lang= 'en')
        end_text = translator_rus.translate(text)
        return end_text