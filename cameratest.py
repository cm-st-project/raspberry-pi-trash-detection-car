from picamera2 import Picamera2, Preview
import time
from libcamera import Transform

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

# picam2.set_controls({"FrameRate": 60})

picam2.start_preview(
    Preview.QTGL,
    width=800,
    height=600,
    #transform=Transform(vflip=1)
    )
picam2.start()

print('sleeping')
time.sleep(10)

print('stopping')
picam2.stop_preview()
picam2.stop()

print('done')


#picam2.capture_file("test.jpg")