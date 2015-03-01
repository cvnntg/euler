"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.
 
For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.
 
What is the total of all the name scores in the file?
"""

import time

start = time.time()

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
names = open("p022", "r").read().translate(None,"\"").split(",")
names.sort()

sum = 0

for x in xrange(0, len(names)):
	score = 0
	for y in names[x]:
		score += LETTERS.index(y) + 1
	sum += score * (x + 1)

print 'Answer: ' + str(sum)
print 'Time:   ' + '{:0.2f}'.format(time.time()-start) + 's'