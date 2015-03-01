"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:
 
012   021   102   120   201   210
 
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

import time
import math
duration = time.time()

n = 1000000

cur = 0
num = range(10)
ans  = []
lexico  = ''

while len(num) > 0:
	i = 0
	found = False
	while not found:
		fact = math.factorial(len(num)-1)	
		if fact * (i+1) + cur >= n:
			cur += i * fact
			found = True
			ans.append(num[i])
			num.pop(i)
		else:
			i += 1 

for x in ans:
	lexico += str(x)

duration = time.time() - duration

print 'Answer: ' + lexico
print 'Time:   ' + '{:0.2f}'.format(duration) + 's'