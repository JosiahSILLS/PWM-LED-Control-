import time
import board
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 1)

color = [156, 200, 255]
delay = 0.05
def fade_out(color, delay = 0.005):
    if delay <= 0:
        delay = 1
    fadeR = color1[0] / 256.0
    fadeG = color1[1] / 256.0
    fadeB = color1[2] / 256.0
    np.fill(color1)
    np.show()
    
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        np.show()
        print(i, color, fadeR*i, fadeG*i, fadeB*i)
        time.sleep(delay)
        
def fade_in(color, delay = 0.005):
    if delay <= 0:
        delay = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0, 0, 0]
    np.fill(color1)
    np.show()
    print(color1)
    
    for i in range(256):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        print(i, color, fadeR*i, fadeG*i, fadeB *i)
        time.sleep(delay)
        
def sparkle(color = [0, 0, 0], delay = 1, times = 2):
    for i in range(times):
        np.fill(color)
        np.show()
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = [255, 0, 0]
        np[led2] = [0, 0, 255]
        np[led3] = [255, 255, 255]
        np.show()
        time.sleep(0.1)
        
def chase(color = [0,0,0], delay = 0.1):
    for j in range(30):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = [0,0,255]
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = color
                print("fColor",i,np[i])
            time.sleep(delay)
        
while True:
    chase(color, delay)
    sparkle(color)
    fade_in(color)
    fade_out(color)
