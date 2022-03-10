import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

# Define GPIO pins
GPIO_PINS = (14, 15, 18)
DIR = 20
STEP = 21

# Create the A4988 Nema motor object
A4988 = RpiMotorLib.A4988Nema(DIR, STEP, GPIO_PINS, "A4988")

# Start the motor
A4988.motor_go(False, "Full", 5000, .01, False, .05)

# Clean up GPIO
GPIO.cleanup()
