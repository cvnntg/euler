def getDivisors(x):
	from math import sqrt
	divisors = [1]
	for i in range(2, int(sqrt(x)) + 1):
		if (x % i == 0):
			if i not in divisors:
				divisors.append(i)
			if x/i not in divisors:
				divisors.append(x/i)
	divisors.sort()
	return divisors

def sumDivisors(n):
	return sum(getDivisors(n))

if __name__ == '__main__':
	import time
	duration = time.time()
	
	total = 0
	num   = 9999
	div   = [0] * (num + 1)
	amic  = 0
	
	for x in range(1, num+1):
		div[x] = sumDivisors(x)
	
	for x in range(1, num+1):
		a = div[x]
		if a < num+1:
			if x == div[a] and x != a:
				amic += x
	
	duration = time.time() - duration
	
	print 'Answer: ' + str(amic)
	print 'Time:   ' + '{:0.2f}'.format(duration) + 's'