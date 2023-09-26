import time
from threading import Thread
from vidgear.gears import WriteGear

class RTSPOutput(Thread):
    def __init__(self, fps: int, location: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._should_exit = False
        self._latest_frame = None
        self._timestep = 1.0 / fps
        output_params = {
            "-f": "rtsp",
            "-rtsp_transport": "tcp",
            "-r": fps,
            "-input_framerate": fps
        }
        
        self._stream = WriteGear(
            output = location, 
            logging = False, 
            compression_mode = True, 
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
            if diff < self._timestep:
                time.sleep(self._timestep - diff)

        self._stream.close()

    def stop(self):
        self._should_exit = True