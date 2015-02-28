import math

sum = 0

for i in xrange(3, 1000000):
	factSum = 0
	for j in str(i):
		factSum += math.factorial(int(j))
	if factSum == i:
		sum += i
print sum

# 40730
