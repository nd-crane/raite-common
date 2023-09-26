import pytest
from raite.inputs.stream import StreamInput
import time


def test_initialization():
    stream = StreamInput("tests/test_resources/sample.avi")
    assert stream.isOpened() == True

    with pytest.raises(Exception):
        StreamInput("invalid_path.avi")


def test_frame_capture():
    stream = StreamInput("tests/test_resources/sample.avi")

    stream.start()

    # Capture a few frames
    time.sleep(1)

    # Verify that the latest frame is not None
    timestamp, frame = stream.latest()
    assert frame is not None

    stream.stop()
    stream.join()


def test_thread_exit():
    stream = StreamInput("tests/test_resources/sample.avi")

    stream.start()

    stream.stop()

    stream.join()

    assert stream.isOpened() == False


def test_frame_dimensions():
    stream = StreamInput("tests/test_resources/sample.avi")

    assert stream.width() > 0
    assert stream.height() > 0
