import time
import board
import neopixel
import random

np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 1)

color = [156, 200, 255]
delay = 0.05
blue = [0, 0, 255]
red = [255, 0, 0]
purple = [255, 0, 255]
green = [0, 255, 0]
white = [255, 255, 255]
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
def sparkle(color = [0, 0, 0], delay = 1, times = 10):
    for i in range(times):
        np.fill(color)
        np.show()
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        np[led1] = [255, 255, 255]
        np[led2] = [0, 0, 255]
        np.show()
        time.sleep(0.1)
'''

Function: chase()

Description: Takes in the background color which is black or off then increments the lights in values off 2 or three depending on what is chosen or written in the code creating the illusion of chasing effect. 

Parameters: color, delay

Return value: None 

'''           
def chase(color = [0,0,0], delay = 0.01):
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
    fade_in(blue)
    chase(color)
    fade_out(blue)
    fade_in(white)
    sparkle(color)
    fade_out(blue)
    fade_in(white)
