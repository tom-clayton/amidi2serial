
import alsaseq
import serial
import sys

if len(sys.argv) < 2:
    print("Enter serial port as command line argument.")
    sys.exit()

synth = serial.Serial(port=sys.argv[1], baudrate= 31250, timeout=1)
alsaseq.client("serial", 1, 0, False)
channel = 0

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

while True:
    if alsaseq.inputpending():
        ev = list(alsaseq.input())
        print(ev)
        if ev[0] == 6: #Note on
            print(f'0x{144+channel:x}')
            print(f'0x{ev[7][1]:x}')
            print(f'0x{ev[7][2]:x}')
            synth.write(bytes([144+channel, ev[7][1], ev[7][2]]))
            
        elif ev[0] == 7: #Note off
            print(f'0x{128+channel:x}')
            print(f'0x{ev[7][1]:x}')
            print(f'0x{ev[7][2]:x}')
            synth.write(bytes([128+channel, ev[7][1]], ev[7][2]]))
