"""
Example of using the StreamInput class to read frames from a video file.

Usage:
    $ python example_input.py
"""

import cv2
from raite.inputs.stream import StreamInput


def main():
    stream_input = StreamInput(location="example.mp4")

    stream_input.start()

    while stream_input.isOpened():
        latest_data = stream_input.latest()

        if latest_data is not None:
            timestamp, frame = latest_data

            # Display the frame
            cv2.imshow("Frame", frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    stream_input.stop()

    # Release OpenCV window
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
