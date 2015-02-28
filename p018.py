import time

duration = time.time()
tri = open ('018', 'r')
tri = tri.readlines()
for x in range(0, len(tri)):
	tri[x] = tri[x].split();
for x in range(0, len(tri)):
	for y in range(0, len(tri[x])):
		tri[x][y] = int(tri[x][y])

for x in range(len(tri)-2, -1, -1):
	for y in range(0, len(tri[x])):
		left = tri[x][y] + tri[x+1][y]
		right = tri[x][y] + tri[x+1][y+1]
		tri[x][y] = left
		if right > left:
			tri[x][y] = right
duration = time.time() - duration

print 'Answer: ' + str(tri[0][0])
print 'Time:   ' + str(duration)
