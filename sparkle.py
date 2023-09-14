import time
import board
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = True, brightness = 1)

color = [0, 0, 255]
color1 = [color[0], color[1], color[2]]
np.fill(color1)
def sparkle(color = [0, 0, 0], speed = 1, times = 2):
    for j in range(times):
        np.fill(color)
        np.show()
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = [255, 0, 0]
        np[led2] = [0, 0, 255]
        np[led3] = [255, 255, 255]
        time.sleep(0.1)
        
while True:
    sparkle(color)
