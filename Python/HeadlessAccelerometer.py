import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = Adafruit_LSM303.LSM303()
x = 0
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height

padding = 3
top = padding
bottom = height-padding
left = padding
right = width-padding

image = Image.new('1', (width, height))
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
maxFontWidth, maxFontHeight = font.getsize("x:-99.99")

centerX = (width + maxFontWidth + padding)//2
centerY = (height + maxFontHeight + padding)//2
circleRad = 4


def constrain(val, minVal, maxVal):
    if val < minVal: 
        val = minVal
    elif val > maxVal: 
        val = maxVal
    return val

while True:
  draw.rectangle((0,0,width,height), outline=0, fill=0)
  
  accel, mag = lsm303.read()
  # Grab the X, Y, Z components from the reading and print them out.
  accel_x, accel_y, accel_z = accel
  circleX, circleY = constrain(centerX - accel_y/10, maxFontWidth + padding, width), constrain(centerY - accel_x/10, 0, height - (maxFontHeight + padding))
  draw.ellipse((circleX-circleRad, circleY-circleRad, circleX+circleRad, circleY+circleRad), outline = 255, fill = 0)
  '''
  draw.text((x, top),    "x: " + (str(round(accel_x/107, 3))),  font=font, fill=255)
  draw.text((x, top+20), "y: " + (str(round(accel_y/107, 3))), font=font, fill=255)
  draw.text((x, top+40), "z: "  + (str(round(accel_z/107, 3))), font=font, fill=255)
  '''
  
  draw.text((left, height//2 - maxFontHeight//2), "x:" + str(round(accel_y/107, 3)), font=font, fill=255)
  draw.text((width//2 - maxFontWidth//2, bottom), "y:" + str(round(accel_x/107, 3)), font=font, fill=255)
  
  disp.image(image)
  disp.display()
