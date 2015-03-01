"""
In England the currency is made up of pound, P, and pence, p, and there are eight
coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
It is possible to make P2 in the following way:

1xP1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can P2 be made using any number of coins?
"""

import time
start = time.time()

n = 200
pattern = 0

for i in range(n, -1, -200):
	for j in range(i, -1, -100):
		for k in range(j, -1, -50):
			for l in range(k, -1, -20):
				for m in range(l, -1, -10):
					for o in range(m, -1, -5):
						for p in range(o, -1, -2):
							pattern += 1

print 'Answer: ' + str(pattern)
print 'Time:   ' + '{:0.2f}'.format(time.time()-start) + 's'