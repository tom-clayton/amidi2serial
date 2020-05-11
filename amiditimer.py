#!/usr/bin/env python3

# amiditimer.py - Tom Clayton

# Connect input and out put to alsa midi streams and this program will
# send a message out and time how long it takes for it to return. 

import alsaseq
import sys
import time
import threading

returned = False
time_ms = [0]

def listen(result):
	while True:
		if alsaseq.inputpending():
			event = alsaseq.input()
			if event[0] == 6:
				result[0] = ((time.time_ns() - start) / 1000000)
				return
				

alsaseq.client('Midi Timer', 1, 1, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

# data = (channel, note, velocity, ??, ??)

listen_thread = threading.Thread(target=listen, args=(time_ms,))
listen_thread.start()

out_event = (6, 1, 0, 253, (0, 0), (0, 0), (0, 0), (0, 60, 127, 0, 0))

input("Midi Timer, connect then hit enter to start.")
alsaseq.output(out_event)
start = time.time_ns()

listen_thread.join()

print (f"{time_ms[0]} ms")
            
        

