pandigitalList = []

def pandigitalize(number):
	pandigital = True
	if number.count(str(0)) > 0:
		pandigital = False
	else:
		for i in number:
			if number.count(i) > 1:
				pandigital = False
	return pandigital

for x in xrange(0, 50000):
	if pandigitalize(str(x)):
		for z in xrange(1, x):
			if x % z == 0 and len(str(z) + str(x) + str(x/z)) == 9:
				if pandigitalize(str(z) + str(x) + str(x / z)) and x not in pandigitalList:
					pandigitalList.append(x)
					print x, z, (x/z)
print sum(pandigitalList)

# 45228