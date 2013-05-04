Primitive C64 joystick to Arduino adapter
=========================================

Pinout
------

The following pins should be connected.

 - Ground (there's one next to digital 13) to Joystick A and B pin 8
 - Digital 13 to Joystick A pin 1
 - Digital 12 to Joystick A pin 2
 - Digital 11 to Joystick A pin 3
 - Digital 10 to Joystick A pin 4
 - Digital 9 to Joystick B pin 1
 - Digital 8 to Joystick B pin 2
 - Digital 9 to Joystick B pin 3
 - Digital 6 to Joystick B pin 4
 
Building without Arduino IDE
----------------------------

	$ wget https://github.com/dnet/arscons/raw/master/SConstruct
	$ scons build

Uploading without Arduino IDE
-----------------------------

### Default config ###

	$ scons upload

### Example for ATmega168-based boards ###

	$ ARDUINO_BOARD=atmega168 scons upload

Dependencies for arscons build process
--------------------------------------

 - Arduino libraries 1.0+ (if you have an older version, rename `*.{ino -> pde}`, Debian/Ubuntu package: `arduino-core`)
 - Scons (Debian/Ubuntu package: `scons`)

License
-------

The whole project is available under MIT license.

Known limitations
-----------------

 - it only reads the direction, and ignore fire and other buttons
 - it uses pin 13 for input, so there could be problems with boards having an LED connected to it
