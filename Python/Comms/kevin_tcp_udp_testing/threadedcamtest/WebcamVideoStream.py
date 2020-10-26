from threading import Thread, Lock
from imutils.video import VideoStream

import cv2


class CameraStream(object):
    def __init__(self, src=0):
        # self.stream = cv2.VideoCapture(src)
        # self.stream.set(3, 256)
        # self.stream.set(4, 144)
        
        self.stream = VideoStream(usePiCamera=True, resolution=(256,144),framerate=32).start()
        self.frame = self.stream.read()
        self.started = False
        self.read_lock = Lock()

    def start(self):
        if self.started:
            print("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=(), daemon=True)
        self.thread.start()
        return self

    def update(self):
        while self.started:
            frame = self.stream.read()
            self.read_lock.acquire()
            self.frame =frame
            self.read_lock.release()

    def read(self):
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self):
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback):
        self.stream.release()