
import alsaseq

SPLIT_KEY = 60 #C2

alasseq.client('Keyboard Splitter', 1, 1, False)

# alsaseq event:
# (type, flags, tag, queue, time stamp, source, destination, data)

while True:
    if alsaseq.inputpending():
        event = list(alsaseq.input())
        if (event[0] == 6 or event[0] == 7) and event[7][1] > SPLIT_KEY:
            event[7][0] += 1
        alsaseq.output(event)
            
        

