import time
import board
import neopixel

np = neopixel.NeoPixel(board.D2, 30, auto_write = True, brightness = 1)

color = [0, 0, 255]
color1 = [color[0], color[1], color[2]]
np.fill(color1)
fadeR = color[0] / 256.0
fadeG = color[1] / 256.0
fadeB = color[2] / 256.0
while True:
    for i in range(256):
        color1[0] = int (color[0] - (fadeR * i))
        color1[1] = int (color[1] - (fadeG * i))
        color1[2] = int (color[2] - (fadeB * i))
        np.fill(color1)
        print(i, color, fadeR*i, fadeG*i, fadeB*i)
        time.sleep(0.001)
    for i in range(256):
        color1[0] = int (fadeR * i)
        color1[1] = int (fadeG * i)
        color1[2] = int (fadeB * i)
        np.fill(color1)
        print(i, color, fadeR*i, fadeG *i, fadeB * i)
        time.sleep(0.001)
