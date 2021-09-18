# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan
# Demo of input polarity inversion using a TCA9534 bus-expander
#
# SPDX-License-Identifier: MIT

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
port_config = [1, 1, 1, 1, 1, 1, 1, 1]

# Set port configuration
tca9534.set_port_mode(port_config)

# Invert GPIO four polarity
tca9534.set_gpio_invert(4, 1)

# Get GPIO four status
gpio_four_status = tca9534.get_gpio(4)

# Print GPIO four status
print("GPIO four status: {0}".format(gpio_four_status))
