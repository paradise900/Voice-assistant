from handlers import thanks, wiki, bye, youtube, joke
from voice import voice
import datetime


COMMANDS = [
    {'id': 0, 'text': 'спасибо', 'handler': thanks},
    {'id': 1, 'text': 'найди на википедии', 'handler': wiki},
    {'id': 2, 'text': 'открой ютуб', 'handler': youtube},
    {'id': 3, 'text': 'расскажи шутку', 'handler': joke},
    {'id': 4, 'text': 'пока', 'handler': bye}
]

ACTIVATION = 'джарвис'


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        voice.text_to_speech("Доброе утро, сэр!")
    elif hour >= 12 and hour < 18:
        voice.text_to_speech("Добрый день, сэр!")   
    else:
        voice.text_to_speech("Добрый вечер, сэр!")  
    
    assname = "Джарвис"
    voice.text_to_speech(f"Я ваш голосовой ассистент {assname}")


class Command:
    def __init__(self, text):
        self.text = text
        self.map()

    def map(self):
        if self.text.startswith(ACTIVATION):
            self.text = self.text.replace(ACTIVATION, '').strip()
            for cmd in COMMANDS:
                if self.text.startswith(cmd['text']):
                    self.run(cmd)
                    return True
            else:
                voice.text_to_speech('Я не знаю такой команды')


        
    def run(self, cmd):
        handler = cmd['handler']
        handler(self.text)
