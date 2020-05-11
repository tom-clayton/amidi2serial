#!/usr/bin/env python3

# amidi2serial.py - Tom Clayton

# Connect input and alsa midi stream and set output to a  serial port.
# This program will send note on and note off messages recevied on
# the midi stream to the serial port. Serial port is set with a command
# line input.

import alsaseq
import serial
import sys

if len(sys.argv) < 2:
    print("Enter serial port as command line argument.")
    sys.exit()

synth = serial.Serial(port=sys.argv[1], baudrate= 31250, timeout=1)
alsaseq.client("Midi to Serial", 1, 0, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

# data = (channel, note, velocity, ??, ??)

while True:
    if alsaseq.inputpending():
        event = list(alsaseq.input())
        #print(event)
        if event[0] == 6: #Note on
            print(f'0x{144+event[7][0]:x}')
            print(f'0x{event[7][1]:x}')
            print(f'0x{event[7][2]:x}')
            synth.write(bytes([144+event[7][0], event[7][1], event[7][2]]))
            
        elif event[0] == 7: #Note off
            print(f'0x{128+event[7][0]:x}')
            print(f'0x{event[7][1]:x}')
            print(f'0x{event[7][2]:x}')
            synth.write(bytes([128+event[7][0], event[7][1]], event[7][2]]))
