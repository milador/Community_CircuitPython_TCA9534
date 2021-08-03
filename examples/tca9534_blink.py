# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan
# Demo of blinking or changing a GPIO's status every second using a TCA9534 bus-expander

from adafruit_bus_device.i2c_device import I2CDevice
import board
import busio
import time 
import community_tca9534

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create bus-expander instance.
tca9534 = community_tca9534.TCA9534(i2c)

# Set GPIO three configuration (OUTPUT)
gpio_three_mode = tca9534.set_gpio_mode(3,0)

# Main loop blinks and prints the GPIO three status every second:
while True:
    gpio_three_status = tca9534.set_gpio(3,0)
    print("GPIO three status: LOW")
    # Delay for one second.
    time.sleep(1.0)
    gpio_three_status = tca9534.set_gpio(3,1)
    print("GPIO three status: HIGH")
    # Delay for one second.
    time.sleep(1.0)