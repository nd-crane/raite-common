import time
from threading import Thread
from vidgear.gears import WriteGear


class RTSPOutput(Thread):
    def __init__(
        self,
        location: str,
        fps: int = 30,
        verbose: bool = False,
        compressed: bool = True,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._should_exit = False
        self._latest_frame = None
        self._timestep = 1.0 / fps
        output_params = {"-f": "rtsp", "-rtsp_transport": "tcp"}

        self._stream = WriteGear(
            output=location,
            logging=verbose,
            compression_mode=compressed,
            **output_params
        )

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

        self._stream.close()

    def stop(self):
        self._should_exit = True
