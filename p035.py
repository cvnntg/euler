import math

circularPrimes = [2]

def isPrime(x):
	if x % 2 == 0:
		return False
	else:
		for i in xrange(3, (x / 2), 2):
			if x % i == 0:
				return False
				break
	return True

def isCircularPrime(x):
	if not isPrime(x):
		return False
	else:
		s = str(x)
		if len(s) > 1:
			for i in xrange(1, len(s)):
				s = s[1:] + s[0]
				if not isPrime(int(s)):
					return False
					break
	return True

for k in xrange(3, 1000001, 2):
	if k not in circularPrimes:
		if isCircularPrime(k):
			if k not in circularPrimes:
				circularPrimes.append(k)
				s = str(k)
				if len(s) > 1:	
					for i in xrange(1, len(s)):
						s = s[1:] + s[0]
						if int(s) not in circularPrimes:
							circularPrimes.append(int(s))

print "Circular Primes:",  len(circularPrimes)

# 55
