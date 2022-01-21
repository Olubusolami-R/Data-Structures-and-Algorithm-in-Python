def sortedSquaredArray(array):
    # Write your code here.
	myarr=[0]*len(array)
	#let the smallest be index 0
	smallest=0
	#let the largest be at the end of the array
	largest=len(array)-1
	i=largest
	for num in array:
		if(abs(array[smallest])<abs(array[largest])):
			myarr[i]=array[largest] * array[largest]
			i-=1
			largest-=1
		else:
			myarr[i]=array[smallest] * array[smallest]
			i-=1
			smallest+=1
    return myarr
