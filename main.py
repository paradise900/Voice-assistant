from recognition import Recognaizer
from voice import voice
from commands import Command, wishMe
import time


rec = Recognaizer()
text_gen = rec.listen()
rec.stream.stop_stream()


wishMe()
time.sleep(0.5)
rec.stream.start_stream()
for text in text_gen:
    print(text)
    rec.stream.stop_stream()
    Command(text)
    time.sleep(0.5)
    rec.stream.start_stream()