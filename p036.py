def isPalindrome(s):
	if s[len(s) - 1] is "0":
		return False
	else:
		for i in xrange(0, len(s) / 2):
			if s[i] is not s[len(s) - 1 - i]:
				return False
	return True

sum = 0
for x in xrange(0, 1000000):
	if isPalindrome(str(x)) and isPalindrome(str(bin(x))[2:]):
		sum += x
print sum

# 872187
