import TCA9548A
import board
import adafruit_ssd1306
import time
import random
from PIL import Image

# Create the I2C interface
i2c = board.I2C()

# Select the display
# This display is located inside of the food dispenser extrusion, front and
# center on the machine.
TCA9548A.tcaselect(1); # should be 1

# Create the SSD1306 object
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

def line_drop(thickness, delay, repeat):
    # Clear the display
    display.fill(0)
    display.show()

    # Sweep the screen {repeat} times with the falling food animation
    for fullScreenSweep in range(repeat):
        
        pixelX = 0

        # Repeat the line as many times as possible within 128 pixels
        for i in range(int(128/thickness)):
        
            # Clear the display; remove the previously drawn frame
            display.fill(0)

            # Set the brightness
            display.contrast(100)

            # Create a {thickness}-pixel-thick line
            for j in range(thickness):
                pixelX += 1
                # Create the line
                display.line(pixelX, 0, pixelX, 32, 1)

            # Show the line
            display.show()

            # Wait a little
            time.sleep(delay)

        # Clear the display
        display.fill(0)
        display.show()

def glowdrop(repeat):
        display.fill(0)
        display.show()

        display.contrast(100)

        for sweep in range(repeat):
            for frame in range(25):
                pathToImage = "animation/glowdrop/glowdrop_" + str(frame) + ".bmp"
                image = Image.open(pathToImage)
                img = image.convert("1")
                display.image(img)
                display.show()
                time.sleep(0.03)

        display.fill(0)
        display.show()

def glowing_alert(repeat):
    display.fill(0)
    display.show()

    # Set display brightness to lowest setting
    display.contrast(0)

    # Increase brightness to max, wait a moment, then go back to 0 repeatedly
    for glow in range(repeat):

        # First, increase brightness artificially using a series of images
        # each with an increasing number of white pixels. This allows
        # an extended range of brightness.
        for level in range(10):
            pathToImage = "animation/brightness/brightness_" + str(level) + ".bmp"
            image = Image.open(pathToImage)
            img = image.convert("1")
            display.image(img)
            display.show()
            time.sleep(0.025)

        # Second, increase display brightness on a full white screen
        # from 0 to 100.
        for level in range(0, 100, 2):
            display.contrast(level)
            display.show()
            time.sleep(0.015)

        # Wait a little
        time.sleep(0.25)

        # Display brightness in reverse
        for level in range(99, -1, -2):
            display.contrast(level)
            display.show()
            time.sleep(0.015)

        # Artificial brightness images in reverese
        for level in range(9, -1, -1):
            pathToImage = "animation/brightness/brightness_" + str(level) + ".bmp"
            image = Image.open(pathToImage)
            img = image.convert("1")
            display.image(img)
            display.show()
            time.sleep(0.025)

        time.sleep(0.15)

        # Full black
        display.fill(0)
        display.show()

glowing_alert(3)
glowdrop(6)
