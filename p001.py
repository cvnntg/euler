"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
 
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time

start = time.time()

n = 1000

print 'Answer: ' + str(sum(set(list(range(0, n, 3))+list(range(0, n, 5)))))
print 'Time:   ' + '{:0.2f}'.format(time.time()-start) + 's'