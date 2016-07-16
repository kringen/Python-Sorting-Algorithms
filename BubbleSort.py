#####################################################################
## This is a simple example of how the bubble sort algorithm works
#####################################################################  
def bubblesort(arr):
	# Start with the next to last array index
	maxIndex = len(arr) - 1
	# Set the initial state of swap to true
	swap = True
	#  Set the passNumber to 1
	passNumber = 1
	while maxIndex > 0 and swap:
		print("passNumber: " + str(passNumber))
		passNumber += 1
		# Set swap to false as default
		swap = False
		for i in range(maxIndex):
			a = arr[i]
			b = arr[i+1]
			if b < a: # swap a and b
				arr[i] = b
				arr[i+1] = a
				#  Indicate that a swap took place so the loop continues
				swap = True
		# Decrement the index
		maxIndex -= 1
		print(arr)

# Note the difference between an array like this with low numbers to high numbers		
arr1 = [3, 2, 6, 4, 9, 4, 3, 7, 8, 5, 3, 5, 78, 54, 102]
# Compared to an array that is almost reverse sorted...Takes more iterations!
arr2 = [100, 54, 78, 5, 3, 8, 7, 3, 4, 9, 4, 6, 2, 3]
bubblesort(arr1)
bubblesort(arr2)      
    
