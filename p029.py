a = []
x = 2
y = 5
for i in xrange(x, y + 1):
	for j in xrange(x, y + 1):
		if i ** j not in a:
			a.append(i ** j)

print len(a)

# 9183