import pyaudio
import sounddevice
from vosk import Model, KaldiRecognizer


class AudioControl:
    def __init__(self):