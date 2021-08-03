# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan
# Demo of input polarity inversion second test using a TCA9534 bus-expander

from adafruit_bus_device.i2c_device import I2CDevice
import board
import busio
import time 
import community_tca9534

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create bus-expander instance.
tca9534 = community_tca9534.TCA9534(i2c)

# Create port configuration array ( 1 = INPUT , 0 = OUTPUT )
port_config=[1,1,1,1,1,1,1,1]

# Create port inversion array ( 1 = INVERT , 0 = NORMAL )
port_polarity=[0,1,0,0,0,0,0,0]

# Set port configuration
tca9534.set_port_mode(port_config)

# Invert GPIO one polarity
tca9534.set_port_invert(port_polarity)

# Get GPIO one polarity
gpio_one_polarity = tca9534.get_gpio_invert(1)

# Print GPIO one polarity
print("GPIO one polarity: {0}".format(gpio_one_polarity))

# Get GPIO one status
gpio_one_status = tca9534.get_gpio(1)

# Print GPIO one status
print("GPIO one status: {0}".format(gpio_one_status))