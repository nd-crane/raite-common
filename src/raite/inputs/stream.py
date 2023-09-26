import cv2
from threading import Thread

class StreamInput(Thread):
    _stream: cv2.VideoCapture
    _should_exit: bool = False

    # Latest Information
    _latest_timestamp = 0.0

    def __init__(self, location: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._latest_frame = None

        # Initialize Stream
        self._stream = cv2.VideoCapture(location)
        if not self._stream.isOpened():
            raise Exception("can't open video writer")

        # Reduce buffer size if supported
        self._stream.set(cv2.CAP_PROP_BUFFERSIZE, 3)

    def isOpened(self) -> bool:
        return self._stream.isOpened()

    def width(self) -> int:
        return int(self._stream.get(cv2.CAP_PROP_FRAME_WIDTH))

    def height(self) -> int:
        return int(self._stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def latest(self):
        if self._latest_frame is None:
            return (None, None)
        return (self._latest_timestamp, self._latest_frame.copy())

    def run(self) -> None:
        while not self._should_exit:
            ret, frame = self._stream.read()
            if not ret:
                break
            self._latest_frame = frame
            self._latest_timestamp = self._stream.get(cv2.CAP_PROP_POS_MSEC)

        self._stream.release()

    def stop(self):
        self._should_exit = True
