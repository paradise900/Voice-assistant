import vosk
import pyaudio
import json


class Recognaizer:
    def __init__(self):
        model = vosk.Model('vosk-model-small-ru-0.22')
        self.rec = vosk.KaldiRecognizer(model, 16000)
        self.start_stream()

    def start_stream(self):
        pa = pyaudio.PyAudio()
        self.stream = pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8000
        )


    def listen(self):
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data) and len(data) > 0:
                res = self.rec.Result()
                answer = json.loads(res)
                if answer['text']:
                    yield answer['text']


if __name__ == '__main__':
    rec = Recognaizer()
    text_gen = rec.listen()
    for text in text_gen:
        print(text)