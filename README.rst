Introduction
============


.. image:: https://readthedocs.org/projects/community-circuitpython-tca9534/badge/?version=latest
    :target: https://circuitpython-tca9534.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/milador/Community_CircuitPython_TCA9534/workflows/Build%20CI/badge.svg
    :target: https://github.com/milador/Community_CircuitPython_TCA9534/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython library for TCA9534 Low Voltage 8-Bit I2C and SMBUS Low-Power I/O Expander with Interrupt Output and Configuration Registers.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/Community-circuitpython-tca9534/>`_.
To install for current user:

.. code-block:: shell

    pip3 install Community-circuitpython-tca9534

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install Community-circuitpython-tca9534

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install Community-circuitpython-tca9534



Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install tca9534

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: shell

    #Demo of reading GPIO's status in TCA9534 bus-expander

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



More examples are available in the examples directory.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/milador/Community_CircuitPython_TCA9534/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
