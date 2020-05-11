#!/usr/bin/env python3

# amidioffset.py - Tom Clayton

# Connect input and out put to alsa midi streams and this program will
# shift midi notes received by x notes. x is set with a command line 
# argument. x can be negative to shift down.

import alsaseq
import sys

if len(sys.argv) > 1:
    offset = int(sys.argv[1])
else:
	print ("Enter offset as command line argument.")
	sys.exit()

alsaseq.client('Midi Offset', 1, 1, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

# data = (channel, note, velocity, ??, ??)

while True:
    if alsaseq.inputpending():
        event = list(alsaseq.input())
        if (event[0] == 6 or event[0] == 7):
            data = list(event[7])
            data[1] += offset 
            event[7] = tuple(data)
        alsaseq.output(event)
            
        

