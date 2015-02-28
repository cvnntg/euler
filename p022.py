import time

start = time.time()

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
names = open("022", "r").read().translate(None,"\"").split(",")
names.sort()

sum = 0

for x in xrange(0, len(names)):
	score = 0
	for y in names[x]:
		score += LETTERS.index(y) + 1
	sum += score * (x + 1)

print sum
print "This took " + str(time.time() - start) + "s."

# 871198282