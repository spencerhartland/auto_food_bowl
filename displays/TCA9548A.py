"""TCA9548A I2C Multiplexer Driver

This python driver uses the System Management Bus (smbus) to communicate with
the TCA948A Multiplexer via I2C and switch between its 8 available channels.
"""

import smbus
import time
import sys

# Create the bus
bus = smbus.SMBus(1)

# Address(es) of TCA9548A Multiplexer
MULTIPLEXER_CH0 = 0x70
MULTIPLEXER_CH1 = 0X74

# TCA Channels
channels = [0b00000001,0b00000010,0b00000100,0b00001000,0b00010000,0b00100000,0b01000000,0b10000000]

def tcaselect(channel):
    """Switches the output of all I2C commands to the selected channel."""
    
    if channel > 7:
        return

    # Allows switching between channels using diff addresses for the multiplexer
    try:
        bus.write_byte(MULTIPLEXER_CH0, channels[channel])
    except OSError:
        bus.write_byte(MULTIPLEXER_CH1, channels[channel])
