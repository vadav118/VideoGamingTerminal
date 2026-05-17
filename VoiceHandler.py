import pyaudio
import sounddevice
import json
from vosk import Model, KaldiRecognizer


class AudioControl:
    model = Model("vosk-model-small-en-us-0.15")
    def __init__(self):
        self.setMicerophone(0)
        self.p = pyaudio.PyAudio()

    def setMicerophone(self,id):
        self.mic = id


    def printAllMicrophones(self):
        for device in sounddevice.query_devices():
            if device['max_input_channels'] > 0 and device['hostapi'] == 0:
                print(f"{device['index']} : {device['name']}")


    def getCurrentMicrophone(self):
        return self.p.get_device_info_by_index(self.mic)

    def run(self):
        current_mic = self.getCurrentMicrophone()
        recognizer = KaldiRecognizer(self.model,int(current_mic['defaultSampleRate']))
        stream = self.p.open(format=pyaudio.paInt16,channels=1,input=True,
                             input_device_index=int(current_mic['index']),rate=int(current_mic['defaultSampleRate']),frames_per_buffer=8192)
        stream.start_stream()
        try:
            while True:
                data = stream.read(8192, exception_on_overflow=False)

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "")

                    if text:
                        print(f"Your command: {text}")
        except KeyboardInterrupt:
            print("\nStopped listening")
        finally:
            stream.stop_stream()
            stream.close()
            self.p.terminate()