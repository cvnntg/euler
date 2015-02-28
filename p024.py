import time
import math
duration = time.time()

current = 0
maxNums = 1000000
numbers = range(10)
answer  = []
stringd = ''

while len(numbers) > 0:
	curIndex = 0
	found = False
	while not found:
		fact = math.factorial(len(numbers)-1)	
		if fact * (curIndex+1) + current >= maxNums:
			current = current + curIndex * fact
			found = True
			answer.append(numbers[curIndex])
			numbers.pop(curIndex)
		else:
			curIndex += 1 

for x in answer:
	stringd += str(x)

duration = time.time() - duration

print 'Answer: ' + stringd
print 'Time:   ' + '{:0.2f}'.format(duration) + 's'
