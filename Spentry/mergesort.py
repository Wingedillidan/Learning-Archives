def merge_sort(left):
	
	# if the list consists of 1 or less things, return
	# <?> Is there a possibility that the list can be less than 1 in this part?
	if len(left) <= 1:
		return left
	
	# finds the middle integer of the input list
	middle = len(left) / 2
	print "The middle is: %i" % middle
	print "The unsplit list is currently: %r" % left
	
	# divides the input list into 2
	right = left[middle:]
	del left[middle:]
	
	print "The left is: %r, the right is: %r.\n" % (left, right)
	
	# recursively run merge_sort on both of the new lists
	# <?> How can you set the list object while using the previously set object in the function?
	left = merge_sort(left)
	right = merge_sort(right)
	
	# returns a merged sorted list
	return merge(left, right)


def merge(left, right):
	
	# declares list to be returned
	# <?> Do I need to declare objects outside of statements and loops?
	# <?> If so, is it because the objects declared within are deleted immediately after the statement/loop?
	result = []
	
	# compares the first values of both lists and adds lowest to list 'result'
	# until 1 or both lists are exhausted
	while left and right:
		if left[0] <= right[0]:
			result.append(left[0])
			del left[0]
		else:
			result.append(right[0])
			del right[0]
	
	# below loops are for when one list is depleted
	# adds any remaining values on the left to the list
	while left:
		result.append(left[0])
		del left[0]
	
	# adds any remaining values on the right to the list
	while right:
		result.append(right[0])
		del right[0]
	
	# prints and returns the merge results
	print "A merge happened! %r\n" % result
	return result


mylist = [7, 2, 1, 4, 9, 3]
print "Final result: %r\n" % merge_sort(mylist)