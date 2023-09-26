# RAITE Common

This repository contains common code for the RAITE project.


## Installation

```bash
virtualenv venv --python=python3.10
source venv/bin/activate
pip install --editable .
```


## Example

The `raite` library can be used to create a pipeline of inputs and outputs. The following example shows how to create a pipeline that takes a stream from an RTSP server and outputs it to another RTSP server.

```python
from raite.inputs.stream import StreamInput
from raite.outputs.rtsp import RTSPOutput


input_stream = StreamInput("rtsp://localhost:8554/test")

output_stream = RTSPOutput("rtsp://localhost:8554/test2")

output_stream.start()
input_stream.start()

while input_stream.isOpened():
  latest_data = input_stream.latest()

  if latest_data is not None:
    timestamp, frame = latest_data
    # This is where you would perform any processing on the frame.
    output_stream.update(frame)

input_stream.join()
output_stream.join()
```
