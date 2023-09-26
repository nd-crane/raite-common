"""
Example for stream rebroadcasting.

Usage:
    $ python rebroadcast_stream.py --input "input_stream_location" --output "output_rtsp_location" --fps 30
"""

import argparse

from raite.inputs.stream import StreamInput
from raite.outputs.rtsp import RTSPOutput


def main(input_location: str, output_location: str, fps: int):
    # Initialize the StreamInput and RTSPOutput classes
    stream_input = StreamInput(input_location)
    rtsp_output = RTSPOutput(output_location, fps=fps)

    # Start the threads
    stream_input.start()
    rtsp_output.start()

    try:
        while True:
            # Retrieve the latest frame
            latest_frame = stream_input.latest()

            if latest_frame is not None:
                _, frame = latest_frame
                print(frame.shape)
                # This is where you would perform any processing on the frame.
                rtsp_output.update(frame)

    except KeyboardInterrupt:
        print("Stopping stream...")
    finally:
        stream_input.stop()
        rtsp_output.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rebroadcast a video stream.")

    parser.add_argument(
        "-i", "--input", required=True, help="Input video stream location."
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output RTSP stream location."
    )
    parser.add_argument(
        "-f",
        "--fps",
        type=int,
        default=30,
        help="Frames per second for the output stream. Default is 30.",
    )

    args = parser.parse_args()

    main(args.input, args.output, args.fps)
