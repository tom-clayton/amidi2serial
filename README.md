# Midi Utils

# amidi2serial

Links an alsa midi output to a serial port.

Port is set with a command line argument, i.e. /dev/ttyACM3

Requires alsaseq and pyserial:

pip install alsaseq
pip install pyserial

Needs manually connecting with aconnect, once running.

# amidisplitter

Increments the channel of incoming midi note messages if they are above a set note.

Note is set with a command line argument of the midi note number, else it will default to C4 (60).

Requires alsaseq:

pip install alsaseq

Needs manually connecting with aconnect, once running.

