import board
import neopixel
import random
import time

np = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write = False, brightness = 1)

color = [0, 0, 0]
delay = 0.05
blue = [0, 0, 255]
red = [255, 0, 0]
purple = [255, 0, 255]
green = [0, 255, 0]
white = [255, 255, 255]
orange = [255, 165, 0]
'''

Function: fade_out()

Description: This function decreases the brightness of a selected color from the max to the minimum brightness slowly.

Parameters: color, delay

Return value: Prints the color values whenever they update. 

'''
def fade_out(color, speed=0.01):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: fade_in()

Description: This function incremently increases the brightness of a selected color from the minimum to the maximum brightness slowly.

Parameters: color, delay

Return value: Prints the color values whenever they update. 

'''        
def fade_in(color, speed=0.01):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0,0,0]
    np.fill(color1)
    np.show()
    print(color1)
    for i in range(255):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        np.show()
        time.sleep(speed)
        print(color1)

'''

Function: sparkle()

Description: The funtion takes blank background ([0, 0, 0]), then displays a chosen color at random intervals and at random positions on the LED strip

Parameters: color, delay and times

Return value: None 

'''        
def sparkle(color = [0, 0, 0], delay = 1, times = 20):
    for i in range(times):
        np.fill(color)
        np.show()
        led1 = random.randint(0, 8)
        led2 = random.randint(0, 8)
        np[led1] = [255, 165, 0]
        np[led2] = [0, 255, 0]
        np.show()
        time.sleep(0.1)
'''

Function: chase()

Description: Takes in the background color which is black or off then increments the lights in values off 2 or three depending on what is chosen or written in the code creating the illusion of chasing effect. 

Parameters: color, delay

Return value: None 

'''           
def chase(color = [0,0,0], delay = 0.01):
    for j in range(10):
        np.show()
        for i in range(10):
            if i % 3 != 0:
                led = (i+j) % 10 
                np[led] = [0, 255, 0]
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 10
                np[led] = color
                print("fColor",i,np[i])
            time.sleep(delay)
'''

Function: fire()

Description: Randomly sparkles a selected color or colors to create the illusin of fire.  

Parameters: color, delay, and times

Return value: None 

'''            
def fire(color = [255, 0, 0], delay = 1, times = 30):
    for i in range(times):
        np.fill(color)
        np.show()
        led1 = random.randint(0, 8)
        led2 = random.randint(0, 8)
        led3 = random.randint(0, 8)
        led4 = random.randint(0, 8)
        led5 = random.randint(0, 8)
        led6 = random.randint(0, 8)
        led7 = random.randint(0, 8)
        np[led1] = [255, 40, 3]
        np[led2] = [255, 60, 3]
        np[led3] = [0, 0, 0]
        np[led4] = [255, 40, 3]
        np[led5] = [255, 40, 3]
        np[led6] = [255, 30, 3]
        np[led7] = [255, 30, 3]
        np.show()
        time.sleep(0.2)
        
        
while True:
    fade_in(green)
    fade_out(green)
    fade_in(purple)
    fade_out(purple)
    sparkle(color)
    fire(color)
