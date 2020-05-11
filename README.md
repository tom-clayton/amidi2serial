# Midi Utils

A selection of useful alsa midi apps using alsaseq.

Requires python module alsaseq, which requires libasound-dev.

For Debian:

sudo apt install libasound-dev

pip3 install alsaseq

Apps need manually connecting with aconnect, once running.

# amidi2serial

Links an alsa midi output to a serial port.

Port is set with a command line argument, i.e. /dev/ttyACM3

Requires pyserial:

pip3 install pyserial

# amidisplitter

Increments the channel of incoming midi note messages if they are above 
a set note. Note is set with a command line argument of the midi note 
number, else it will default to B3 (59).

# amidioffset

Shifts midi note by a set value. Value is set with a command line 
argument. Value can be negative.

# amidimonitor

Prints note on and note off messages to command line in hexidecimal.

# amiditimer

Times a midi message round trip in milliseconds.

To come...

Midi clock from beat

