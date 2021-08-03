# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Milad Hajihassan for Milador
#
# SPDX-License-Identifier: MIT
"""
`community_tca9534`
================================================================================

CircuitPython library for TCA9534 Low Voltage 8-Bit I2C and SMBUS Low-Power I/O Expander with Interrupt Output and Configuration Registers.


* Author(s): Milad Hajihassan

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s).
  Use unordered list & hyperlink rST inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies
  based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports
import adafruit_bus_device.i2c_device as i2c_device
from micropython import const

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/milador/Community_CircuitPython_TCA9534.git"

TCA9534_DEFAULT_I2C_ADDR        = const(0x27)
TCA9534_REGISTER_INPUT_PORT     = const(0x00)
TCA9534_REGISTER_OUTPUT_PORT    = const(0X01)
TCA9534_REGISTER_INVERSION      = const(0x02)
TCA9534_REGISTER_CONFIGURATION  = const(0X03)
    
class TCA9534:
    _BUFFER = bytearray(2)
    
    ################################################################################
    #  __init__(self, i2c, address=TCA9534_DEFAULT_I2C_ADDR)
    #
    #  Arguments: i2c, address
    #
    #  Description: Class initialization
    #  
    ################################################################################  
    def __init__(self, i2c, address=TCA9534_DEFAULT_I2C_ADDR):
        self._device = i2c_device.I2CDevice(i2c, address)

    ################################################################################
    #  read_bit(self, register_address, gpio_position)
    #
    #  Arguments: register_address, gpio_position
    #
    #  Description: Read a bit by register address and gpio position
    #  
    ################################################################################  
    def read_bit(self, register_address, gpio_position):
        return ((self.read_register(register_address) & (1 << gpio_position)) >> gpio_position)

    ################################################################################
    #  write_bit(self, register_address, gpio_position, bit_value)
    #
    #  Arguments: register_address, gpio_position, bit_value
    #
    #  Description: Write a bit by register address, gpio position, and bit value
    #  
    ################################################################################  
    def write_bit(self, register_address, gpio_position, bit_value):
        byte_value = self.read_register(register_address)
        bit_mask = 1 << gpio_position
        byte_value = (byte_value & ~bit_mask) | ((bit_value << gpio_position) & bit_mask)
        return self.write_register(register_address, byte_value)

    ################################################################################
    #  read_register(self, address)
    #
    #  Arguments: address
    #
    #  Description: Read a register by register address
    #  
    ################################################################################     
    def read_register(self, address):
        with self._device as i2c:
            self._BUFFER[0] = (address) & 0xFF
            i2c.write_then_readinto(self._BUFFER, self._BUFFER, out_end=1, in_end=1)
        return self._BUFFER[0]

    ################################################################################
    #  write_register(self, address, value)
    #
    #  Arguments: address and value
    #
    #  Description: Write a value by a register address
    #  
    ################################################################################   
    def write_register(self, address, value):
        with self._device as i2c:
            self._BUFFER[0] = (address) & 0xFF
            self._BUFFER[1] = value & 0xFF
            i2c.write(self._BUFFER, end=2)

    ################################################################################
    #  get_gpio_mode(self, gpio_position)
    #
    #  Arguments: gpio_position
    #
    #  Description: Get a gpio mode/configuration by it's position
    #  
    ################################################################################   
    def get_gpio_mode(self, gpio_position):
        port_configuration = self.read_register(TCA9534_REGISTER_CONFIGURATION)
        return True if (port_configuration & (1 << gpio_position)!=0) else False

    ################################################################################
    #  set_gpio_mode(self, gpio_position, gpio_mode)
    #
    #  Arguments: gpio_position, gpio_mode
    #
    #  Description: Set a gpio mode/configuration by it's position
    #  
    ################################################################################  
    def set_gpio_mode(self, gpio_position, gpio_mode):
        port_configuration = self.read_register(TCA9534_REGISTER_CONFIGURATION)
        gpio_mask = 1 << gpio_position
        port_configuration = (port_configuration & ~gpio_mask) | ((gpio_mode << gpio_position) & gpio_mask)
        return self.write_register(TCA9534_REGISTER_CONFIGURATION, port_configuration)

    ################################################################################
    #  get_port_mode(self)
    #
    #  Arguments: None
    #
    #  Description: Get port mode/configuration
    #  
    ################################################################################          
    def get_port_mode(self):
        port_mode_array = []
        port_mode_status = self.read_register(TCA9534_REGISTER_CONFIGURATION)
        for gpio_position in range(8):
            gpio_mode_status = True if (port_mode_status & (1 << gpio_position)!=0) else False
            port_mode_array.append(gpio_mode_status)  
        return port_mode_array

    ################################################################################
    #  set_port_mode(self, port_mode_array)
    #
    #  Arguments: port_mode_array
    #
    #  Description: Set port mode/configuration
    #  
    ################################################################################   
    def set_port_mode(self, port_mode_array):
        port_configuration = 0x0
        for gpio_position in range(len(port_mode_array)):
            port_configuration |= port_mode_array[gpio_position] << gpio_position
        return self.write_register(TCA9534_REGISTER_CONFIGURATION, port_configuration)

    ################################################################################
    #  get_gpio_invert(self, gpio_position)
    #
    #  Arguments: gpio_position
    #
    #  Description: Get gpio inversion polarity
    #  
    ################################################################################  
    def get_gpio_invert(self, gpio_position):
        port_inversion = self.read_register(TCA9534_REGISTER_INVERSION)
        gpio_inversion_status = True if (port_inversion & (1 << gpio_position)!=0) else False
        return gpio_inversion_status

    ################################################################################
    #  set_gpio_invert(self, gpio_position, inversion_mode)
    #
    #  Arguments: gpio_position, inversion_mode
    #
    #  Description: Set gpio inversion polarity
    #  
    ################################################################################          
    def set_gpio_invert(self, gpio_position, inversion_mode):
        port_inversion = self.read_register(TCA9534_REGISTER_INVERSION)
        gpio_mask = 1 << gpio_position
        port_inversion = (port_inversion & ~gpio_mask) | ((inversion_mode << gpio_position) & gpio_mask)
        return self.write_register(TCA9534_REGISTER_INVERSION, port_inversion)
 
    ################################################################################
    #  get_port_invert(self)
    #
    #  Arguments: None
    #
    #  Description: Get port inversion polarity
    #  
    ################################################################################    
    def get_port_invert(self):
        port_inversion_array = []
        port_inversion_status = self.read_register(TCA9534_REGISTER_INVERSION)
        for gpio_position in range(8):
            gpio_inversion_status = True if (port_inversion_status & (1 << gpio_position)!=0) else False
            port_inversion_array.append(gpio_inversion_status)  
        return port_inversion_array

    ################################################################################
    #  set_port_invert(self, inversion_mode_array)
    #
    #  Arguments: inversion_mode_array
    #
    #  Description: Set port inversion polarity
    #  
    ################################################################################   
    def set_port_invert(self, inversion_mode_array):
        port_inversion = 0x0
        for gpio_position in range(len(inversion_mode_array)):
            port_inversion |= inversion_mode_array[gpio_position] << gpio_position
        return self.write_register(TCA9534_REGISTER_INVERSION, port_inversion)

    ################################################################################
    #  get_gpio(self, gpio_position)
    #
    #  Arguments: gpio_position
    #
    #  Description: Get gpio status by gpio position
    #  
    ################################################################################   
    def get_gpio(self, gpio_position):
        port_in_status = self.read_register(TCA9534_REGISTER_INPUT_PORT)
        gpio_in_status = True if (port_in_status & (1 << gpio_position)!=0) else False
        return gpio_in_status

    ################################################################################
    #  set_gpio(self, gpio_position, gpio_out_status)
    #
    #  Arguments: gpio_position, gpio_out_status
    #
    #  Description: Set gpio status by gpio position
    #  
    ################################################################################
    def set_gpio(self, gpio_position, gpio_out_status):
        port_out_status = self.read_register(TCA9534_REGISTER_OUTPUT_PORT)
        gpio_mask = 1 << gpio_position
        port_out_status = (port_out_status & ~gpio_mask) | ((gpio_out_status << gpio_position) & gpio_mask)
        self.write_register(TCA9534_REGISTER_OUTPUT_PORT, port_out_status)
        return self.write_register(TCA9534_REGISTER_OUTPUT_PORT, port_out_status)
    
    ################################################################################
    #  get_port(self)
    #
    #  Arguments: None
    #
    #  Description: Get gpio status for all the pins in the port
    #  
    ################################################################################
    def get_port(self):
        port_in_array = []
        port_in_status = self.read_register(TCA9534_REGISTER_INPUT_PORT)
        for gpio_position in range(8):
            gpio_in_status = True if (port_in_status & (1 << gpio_position)!=0) else False
            port_in_array.append(gpio_in_status)  
        return port_in_array

    ################################################################################
    #  set_port(self, port_out_array)
    #
    #  Arguments: port_out_array
    #
    #  Description: Set gpio status for all the pins in the port
    #  
    ################################################################################
    def set_port(self, port_out_array):
        port_out_status = 0x0
        for gpio_position in range(len(port_out_array)):
            port_out_status |= port_out_array[gpio_position] << gpio_position
        return self.write_register(TCA9534_REGISTER_OUTPUT_PORT, port_out_status)



