from random import randint
from voice import voice
import wikipedia
import webbrowser
import pyjokes
from googletrans import Translator
import requests


wikipedia.set_lang("ru")


def thanks(text):
    options = [
        'без проблем',
        "все в порядке",
        "мне было не сложно",
        "обращайтейсь"
    ]
    num = randint(0, len(options) - 1)
    voice.text_to_speech(options[num])


def wiki(text):
    voice.text_to_speech('Ищу на википедии...')
    text = text.replace("найди на википедии", "")
    results = wikipedia.summary(text, sentences = 3)
    voice.text_to_speech("По информации из википедии")
    print(results)
    voice.text_to_speech(results)


def bye(text):
    voice.text_to_speech('До свидаяния, господин!')
    exit()


def youtube(text):
    voice.text_to_speech("Так точно, открываю ютуб")
    webbrowser.get('safari').open("youtube.com")


def joke(text):
    translator = Translator()
    voice.text_to_speech('Конечно, держи!')
    URL = 'https://v2.jokeapi.dev/joke/Any?type=twopart'
    request_URL = requests.get(URL)
    joke_en = request_URL.json()
    joke_ru = translator.translate(joke_en['setup'] + joke_en['delivery'], dest='ru')
    voice.text_to_speech(joke_ru.text)