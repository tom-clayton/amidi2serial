
import alsaseq
import sys

if len(sys.argv) > 1:
    split_key = sys.argv[1]
else:
    split_key = 60 # Default, C4

alasseq.client('Keyboard Splitter', 1, 1, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

while True:
    if alsaseq.inputpending():
        event = list(alsaseq.input())
        if (event[0] == 6 or event[0] == 7) and event[7][1] > split_key:
            event[7][0] += 1
        alsaseq.output(event)
            
        

