powers = 5;
sum = 0;
for x in xrange(2, 1000000):
	s = str(x)
	temp = 0
	for y in s:
		temp += int(y) ** powers
	if x == temp:
		sum += x
print sum

# 443839