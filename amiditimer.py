#!/usr/bin/env python3

# amiditimer.py - Tom Clayton

# Connect input and output to alsa midi streams and this program will
# send a message out and time how long it takes for it to return. 

import alsaseq
import sys	

alsaseq.client('Midi Timer', 1, 1, True)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

# data = (channel, note, velocity, start, duration)

out_event = (6, 1, 0, 1, (0, 0), (0, 0), (0, 0), (0, 60, 127, 0, 0))
input("Midi Timer, connect then hit enter to start.")
alsaseq.output(out_event)
alsaseq.start()

while True:
	if alsaseq.inputpending():
		event = alsaseq.input()
		if event[0] == 6:
			print(event[4][1] / 1000000, " ms")
			break
		
            
        

