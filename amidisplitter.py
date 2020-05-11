
import alsaseq
import sys

if len(sys.argv) > 1:
    split_key = int(sys.argv[1])
else:
    split_key = 59 # Default, <-B3 C4->

alsaseq.client('Keyboard Splitter', 1, 1, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

while True:
    if alsaseq.inputpending():
        event = list(alsaseq.input())
        if (event[0] == 6 or event[0] == 7) and event[7][1] > split_key:
            data = list(event[7])
            data[0] += 1
            event[7] = tuple(data)
            #event[7][0] += 1
        alsaseq.output(event)
            
        

