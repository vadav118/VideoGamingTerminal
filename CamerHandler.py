import cv2
from cv2_enumerate_cameras import enumerate_cameras
import mediapipe as mp


class CameraControl:
    model = "pose_landmarker_lite.task"
    def __init__(self):
        self.setCamera(0)


    def printAllCameras(self):
        print("Please choose you're Camera")
        for camera_info in enumerate_cameras():
            print(f"{camera_info.index} : {camera_info.name}")

    def setCamera(self, id):
        self.camera = cv2.VideoCapture(id)

    def run(self):
        camera = self.camera
        while camera.isOpened():
            frame = camera.read()

        camera.release()
        cv2.destroyAllWindows()
