# -*- coding: utf-8 -*-
#
# Hiveeyes MicroPython Datalogger
# https://github.com/hiveeyes/hiveeyes-micropython-firmware
#
# (c) 2019 Richard Pobering <richard@hiveeyes.org>
# (c) 2019 Andreas Motl <andreas@hiveeyes.org>
# License: GNU General Public License, Version 3
#
"""
-----
Setup
-----

Just run::

    make setup
    make install-requirements install-framework

to bring everything into shape.

Then, invoke::

    make sketch-and-run

to upload the program and reset the ESP32.
"""


def extend_syspath():
    """
    Extend Python module search path.
    Dependency modules are shipped through the "dist-packages" folder.
    Please populate this folder appropriately as shown above before
    expecting anything to work.
    """
    import sys
    sys.path.append('dist-packages')
    print('[boot.py] INFO: Python module search path is:', sys.path)
    print()


if __name__ == '__main__':

    # Enable heartbeat LED.
    try:
        import pycom
        pycom.heartbeat(True)
    except:
        pass

    # Enable serial interface.
    # Note: Might be done by ``self.device.enable_serial()`` later.
    # import os; from machine import UART
    # uart = UART(0, baudrate=115200); os.dupterm(uart)

    # Extend module search path.
    extend_syspath()
