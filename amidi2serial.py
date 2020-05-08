
import alsaseq
import serial

synth = serial.Serial(port="/dev/ttyACM3", baudrate= 31250, timeout=1)
#synth = serial.Serial(port="/dev/ttyACM4", baudrate=31250, timeout=1)
alsaseq.client("serial", 1, 0, False)
channel = 0

while True:
    if alsaseq.inputpending():
        ev = list(alsaseq.input())
        print(ev)
        if ev[0] == 6:
            print(f'0x{144+channel:x}')
            print(f'0x{ev[7][1]:x}')
            print(f'0x{ev[7][2]:x}')
            synth.write(bytes([144+channel, ev[7][1], ev[7][2]]))
            
        elif ev[0] == 7:
            print(f'0x{128+channel:x}')
            print(f'0x{ev[7][1]:x}')
            print(f'0x{ev[7][2]:x}')
            synth.write(bytes([128+channel, ev[7][1]], ev[7][2]]))
