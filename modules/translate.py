from googletrans import Translator
translator = Translator()
def translate(message, language1, language2):
    result = translator.translate(message.text, src=language1, dest=language2)
    print(f'{message.text} {language1} -> {result.text} {language2}')
    return f'{message.text} {language1} -> {result.text} {language2}'

