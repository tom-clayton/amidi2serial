#!/usr/bin/env python3

# amidimonitor.py - Tom Clayton

# Connect input to an alsa midi stream. This program will print note on
# and note off messages recevied in hexidecimal.

import alsaseq
import sys

alsaseq.client("Monitor", 1, 0, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

# data = (channel, note, velocity, ??, ??)

while True:
    if alsaseq.inputpending():
        event = list(alsaseq.input())
        if event[0] == 6: #Note on
            print(f'0x{0x90+event[7][0]:02x}', end=' ')
            print(f'0x{event[7][1]:02x}', end=' ')
            print(f'0x{event[7][2]:02x}')
            
        elif event[0] == 7: #Note off
            print(f'0x{0x80+event[7][0]:02x}', end=' ')
            print(f'0x{event[7][1]:02x}', end=' ')
            print(f'0x{event[7][2]:02x}')
