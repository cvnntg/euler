digit = []

for i in xrange(10, 100):
	for j in xrange(10, 100):
		a = float(i) / j
		if a < 1:
			w = int(str(i)[0])
			x = int(str(i)[1])
			y = int(str(j)[0])
			z = int(str(j)[1])
			if(y != 0):
				if float(x) / y == a and w == z:
					if digit.count([i, j]) == 0:
						digit.append([i, j])
			if(z != 0):
				if float(w) / z == a and x == y:
					if digit.count([i, j]) == 0:	
						digit.append([i, j])

product = 1.0
for i in digit:
	product *= i[0]
	product /= i[1]
print product

# 100
