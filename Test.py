from VoiceHandler import AudioControl
from CamerHandler import CameraControl

if __name__ == "__main__":
    cam = CameraControl()
    cam.printAllCameras()

    #mic = AudioControl()
    #mic.setMicerophone(4)
    #mic.run()