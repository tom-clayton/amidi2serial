#!/usr/bin/env python3

# amidiclock.py - Tom Clayton

# Sends midi clock data, based on the rate bpm given as a command line
# argument.

import alsaseq
import sys

if len(sys.argv) > 1:
    period = int(60000 / int(sys.argv[1]))
else:
    print("Enter bpm as command line argument.")
    sys.exit()

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

# data = (channel, note, velocity, start, duration)

class MidiClock:
	
	def __init__(self, period):		
		self.period = period
		self.pulse_period = round(period/24)
		self.position = 0
		self.output_pulses()
	
	def check_target(self, status):
		if (status[0]*1000 + status[1]/1000000) > self.target:
			self.position = self.target + self.period
			self.output_pulses() 

	def output_pulses(self):
		for i in range(self.position, 
					   self.position + self.period,
					   self.pulse_period):
			alsaseq.output((alsaseq.SND_SEQ_EVENT_CLOCK, 1, 0, 1,
						   (i // 1000, (i%1000) * 1000000),
						   (0, 0), (0, 0), (0, 0, 0, 0, 0)))
		self.target = self.position
		


alsaseq.client('Midi Clock', 0, 1, True)
alsaseq.start()

midiclock = MidiClock(period)	
			
while True:
	status = alsaseq.status()
	midiclock.check_target(status[1])




            
        

