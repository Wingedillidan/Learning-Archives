def createlist(num, inc):
	i = 0
	numbers = []
	
	for i in range(0, num, inc):
		print "At the top i is %d" % i
		numbers.append(i)
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	return numbers

numlist = createlist(10, 3)

print "The numbers: "

for num in numlist:
	print num