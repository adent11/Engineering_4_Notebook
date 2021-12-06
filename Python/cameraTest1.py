import time
import picamera

print("Camera Test Running")
with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('../Media/camera_test.jpg')
print("Camera Test Done")
