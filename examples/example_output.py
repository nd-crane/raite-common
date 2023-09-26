"""
Example of using the RTSPOutput class to stream frames to an RTSP server.

Usage:
    $ python example_output.py
"""
import numpy as np
from raite.outputs.rtsp import RTSPOutput


def main():
    rtsp_output = RTSPOutput(
        location="rtsp://localhost:8554/mystream", fps=30, verbose=True
    )

    # Start the RTSP stream thread
    rtsp_output.start()

    counter = 0

    while True:
        # Simulate a frame source (e.g. a simple counter on a black background)
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(
            frame,
            str(counter),
            (300, 300),
            cv2.FONT_HERSHEY_SIMPLEX,
            4,
            (255, 255, 255),
            2,
            cv2.LINE_AA,
        )

        rtsp_output.update(frame)

        counter += 1

        if counter >= 100:
            break

    rtsp_output.stop()


if __name__ == "__main__":
    main()
