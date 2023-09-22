import cv2
import time
from threading import Thread

class RTSPOutput(Thread):
    def __init__(self, width: int, height: int, fps: int, location: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._should_exit = False
        self._latest_frame = None
        self._timestep = 1.0 / fps
        self._stream = cv2.VideoWriter('appsrc ! videoconvert' + \
            ' ! video/x-raw,format=I420' + \
            ' ! x264enc speed-preset=ultrafast key-int-max=' + str(fps * 2) + \
            ' ! video/x-h264,profile=baseline' + \
            f' ! rtspclientsink protocols=tcp location={location}',
            cv2.CAP_GSTREAMER, 0, fps, (width, height), True)
        if not self._stream.isOpened():
            raise Exception("can't open video writer")
    
    def update(self, frame):
        self._latest_frame = frame.copy()
        
    def run(self) -> None:
        while not self._should_exit:
            start = time.time()

            if self._latest_frame is not None:
                self._stream.write(self._latest_frame)
            
            diff = time.time() - start
            if diff > self._timestep:
                time.sleep(diff)

        self._stream.release()

    def stop(self):
        self._should_exit = True