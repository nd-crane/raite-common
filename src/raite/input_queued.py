import cv2
import queue
from threading import Thread
from typing import Tuple, Union, Any


class QueuedStreamInput(Thread):
    def __init__(self, location: str, queue_size: int = 10, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize video capture
        self._stream = cv2.VideoCapture(location)
        if not self._stream.isOpened():
            raise Exception("can't open video writer")

        # Reduce buffer size if supported
        self._stream.set(cv2.CAP_PROP_BUFFERSIZE, 3)

        # Initialize exit flag and frame queue
        self._should_exit = False
        self._frame_queue = queue.Queue(maxsize=queue_size)

    def isOpened(self) -> bool:
        return self._stream.isOpened()

    def width(self) -> int:
        return int(self._stream.get(cv2.CAP_PROP_FRAME_WIDTH))

    def height(self) -> int:
        return int(self._stream.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def latest(self) -> Union[None, Tuple[float, Any]]:
        try:
            return self._frame_queue.get_nowait()
        except queue.Empty:
            return None

    def run(self) -> None:
        while not self._should_exit:
            ret, frame = self._stream.read()
            if not ret:
                break

            timestamp = self._stream.get(cv2.CAP_PROP_POS_MSEC)

            # Add the frame and timestamp to the queue
            if not self._frame_queue.full():
                self._frame_queue.put((timestamp, frame))
            else:
                # Remove the oldest frame if the queue is full
                self._frame_queue.get()
                self._frame_queue.put((timestamp, frame))

        self._stream.release()

    def stop(self) -> None:
        self._should_exit = True
