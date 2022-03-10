import TCA9548A
import board
import adafruit_ssd1306
from PIL import Image
import time

# Create the I2C interface
i2c = board.I2C()

# Select the first display
TCA9548A.tcaselect(0) # Should be 0

# Create the SSD1306 object
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

def display_current_food_level(level): # Eventually no parameters
    # NEEDS IMPLEMENTATION
    # Get weight from load cell and compare to reference weight then
    # select the appropriate level to display.

    # Caught in loop when the FCU (Food Containment Unit) is empty, displays
    # a nice animation to get attention and remind you to fill up.
    while level == 0:
        for frame in range(14):
            pathToImage = "food-level/empty-animation/empty_" + str(frame) + ".bmp"
            image = Image.open(pathToImage)
            img = image.convert("1")
            display.image(img)
            display.show()
            time.sleep(0.045)
            # Check weight and break if it goes up from 0

    pathToImage = "food-level/level_" + str(level) + ".bmp"
    image = Image.open(pathToImage)
    img = image.convert("1")
    display.image(img)
    display.show()

for level in range(4, -1, -1):
    display_current_food_level(level)
    time.sleep(3)

display_current_food_level(0)
