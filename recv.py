#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from serial import Serial
from blessings import Terminal
import sys

symbols = ['A↓', 'A↑', 'B→', 'B←', 'B↓', 'B↑', 'A→', 'A←']
port = Serial('/dev/ttyUSB0', 9600, timeout=0.1)
term = Terminal()

try:
	while True:
		serial_data = port.read()
		if serial_data:
			for input_byte in serial_data:
				num = ord(input_byte)
				sys.stdout.write('\r')
				for i, sym in enumerate(symbols):
					pwr = 1 << i
					state = (num & pwr) == pwr
					sys.stdout.write(('..' if state else term.bold_red(sym)) + ' ')
				sys.stdout.flush()
except KeyboardInterrupt:
	pass
finally:
	port.close()
	sys.stdout.write('\n')
