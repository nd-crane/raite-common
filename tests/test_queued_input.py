import pytest
from raite.inputs.queued import QueuedInput
import cv2
import time


def test_initialization():
    # Test with valid video source
    stream = QueuedInput('tests/test_resources/sample.avi')
    assert stream.isOpened() == True

    with pytest.raises(Exception):
        QueuedInput('invalid_path.avi')


def test_queue_management():
    stream = QueuedInput('tests/test_resources/sample.avi', queue_size=2)

    stream.start()

    time.sleep(1)

    # Verify that the queue is not empty
    assert stream.latest() is not None

    stream.stop()
    stream.join()


def test_thread_exit():
    stream = QueuedInput('tests/test_resources/sample.avi')

    stream.start()

    stream.stop()

    stream.join()

    assert stream.isOpened() == False


def test_frame_dimensions():
    stream = QueuedInput('tests/test_resources/sample.avi')

    assert stream.width() > 0
    assert stream.height() > 0
