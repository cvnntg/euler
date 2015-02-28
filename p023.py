import time
from p021 import *

duration = time.time()

num    = 28124
div    = [0]
abund  = []
absums = [False] * (num)
answer = 0

for x in range(1, num):
	div.append(sumDivisors(x))

for x in xrange(1, len(div)):
	if x < div[x]:
		abund.append(x)

for x in xrange(len(abund)):
	for y in xrange(x, len(abund)):
		if abund[x] + abund[y] < num:
			absums[abund[x] + abund[y]] = True
		else:
			break

for x in range(len(absums)):
	if absums[x] == False:
		answer += x

duration = time.time() - duration

print 'Answer: ' + str(answer)
print 'Time:   ' + '{:0.2f}'.format(duration) + 's'