from VoiceHandler import AudioControl
from CamerHandler import CameraControl

if __name__ == "__main__":
    #cam = CameraControl()
    #cam.printCameras()
    mic = AudioControl()
    mic.printAllMicrophones()
    mic.getCurrentMicrophone()