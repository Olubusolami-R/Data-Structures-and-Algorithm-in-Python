def isValidSubsequence(array, sequence):
	i=0
	count=0
	for num in array:
		if num==sequence[i] and i<len(sequence):
			i+=1
			count+=1
		if count==len(sequence):
			return True
	return False
