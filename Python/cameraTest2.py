import time
import picamera

effects = ['solarize', 'sketch', 'denoise', 'emboss', 'oilpaint']

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    for effect in effects:
        camera.image_effect = effect
        camera.capture(f"../Media/imageWith{effect}.jpg")
