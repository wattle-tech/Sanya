from translate import Translator

translator_eng = Translator(from_lang='en', to_lang='ru')
translator_rus = Translator(from_lang='ru', to_lang= 'en')


def translator_en (text:str):
    end_text = translator_eng.translate(text)
    return end_text

def translator_ru (text:str):
    end_text = translator_rus.translate(text)
    return end_text