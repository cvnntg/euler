pattern = 8;

for a in xrange(0, 1):
	for b in xrange(0, 2):
		for c in xrange(0, 4):
			for d in xrange(0, 10):
				for e in xrange(0, 20):
					for f in xrange(0, 40):
						for g in xrange(0, 100):
							for h in xrange(0, 200):
								if (a * 200 + b * 100 + c * 50 + d * 20 + e * 10 + f * 5 + g * 2 + h) == 200:
									pattern += 1
print pattern

# 73682