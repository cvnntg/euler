import math

def isPrime(x):
	if x == 1 or x % 2 == 0:
		return False
	else:
		for i in xrange(3, (x / 2), 2):
			if x % i == 0:
				return False
	return True

def isTrunctablePrime(x):
	if not isPrime(x):
		return False
	else:
		s = str(x)
		for i in xrange(1, len(s)):
			if not isPrime(int(s[0:len(s) - i])) or not isPrime(int(s[i:])):
				return False
	return True

curre = ""
count = 0
upper = 20
need  = 11
trunctablePrimes = []
x     = "13579"

def findTrunctable(digits, more, current):
	if isTrunctablePrime(int(current)):
		if int(current) not in trunctablePrimes:
			trunctablePrimes.append(int(current))
			more += 1
		if digits < upper or more < need:
			for i in x:
				findTrunctable(digits + 1, more, current + i)

findTrunctable(0, 0, "37")
print trunctablePrimes
print "Sum of Trunctable Primes:", sum(trunctablePrimes) 

#
