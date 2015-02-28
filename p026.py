import time
import math
duration = time.time()

num = 1000
sequenceLength = 0;
 
for i in xrange(num, 1, -1):
    if sequenceLength >= i:
        break
 
    foundRemainders = [0] * i
    value = 1
    position = 0
 
    while foundRemainders[value] == 0 and value != 0:
        foundRemainders[value] = position
        value *= 10
        value %= i
        position += 1
 
    if position - foundRemainders[value] > sequenceLength:
        sequenceLength = position - foundRemainders[value]

duration = time.time() - duration

print 'Answer: ' + str(position)
print 'Time:   ' + '{:0.2f}'.format(duration) + 's'