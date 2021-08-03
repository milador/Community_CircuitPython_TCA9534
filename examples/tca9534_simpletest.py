# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan for Milador
# Demo of reading GPIO's status in TCA9534 bus-expander

from adafruit_bus_device.i2c_device import I2CDevice
import board
import busio
import time 
import community_tca9534

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create bus-expander instance.
tca9534 = community_tca9534.TCA9534(i2c)


# Main loop prints the GPIO zero status every half a second:
while True:
    gpio_zero_status = tca9534.get_gpio(0)
    print("GPIO zero status: {0}".format(gpio_zero_status))
    # Delay for half a second.
    time.sleep(0.5)
