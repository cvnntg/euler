"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base
10 and base 2.

(Please note that the palindromic number, in either base, may not include leading
zeros.)
"""

import time

def isPalindrome(s):
	if s[len(s) - 1] is "0":
		return False
	else:
		for i in xrange(0, len(s) / 2):
			if s[i] is not s[len(s) - 1 - i]:
				return False
	return True

start = time.time()

sum = 0
for x in xrange(0, 1000000):
	if isPalindrome(str(x)) and isPalindrome(str(bin(x))[2:]):
		sum += x
		
print 'Answer: ' + str(sum)
print 'Time:   ' + '{:0.2f}'.format(time.time()-start) + 's'