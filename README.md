# Midi Utils

A selection of useful alsa midi apps using alsaseq.

Requires python module alsaseq, which requires libasound-dev.

For Debian:

sudo apt install libasound-dev
pip3 install alsaseq

# amidi2serial

Links an alsa midi output to a serial port.

Port is set with a command line argument, i.e. /dev/ttyACM3

Requires pyserial:

pip3 install pyserial

Needs manually connecting with aconnect, once running.

# amidisplitter

Increments the channel of incoming midi note messages if they are above a set note.

Note is set with a command line argument of the midi note number, else it will default to C4 (60).

Needs manually connecting with aconnect, once running.

To come...

Midi note offset
Midi timer
Midi clock from beat

