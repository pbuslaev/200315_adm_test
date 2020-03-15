import numpy as np

def sortOwn(arr):
	n = arr.size
 
	# Iterate the array
	for i in range(n):
 
		# Last i elements are already in place
		for j in range(0, n-i-1):
 
			# iterate the array from 0 to n-i-1
			# Swap if needed
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

ar = np.array([79, 2, 150, 19, 15],dtype=int) # initialize an array

ar.sort() # sort with in-built function
np.savetxt("sorted1.txt",ar[None], header="In-built sort",fmt='%i')

ar = np.array([79, 2, 150, 19, 15],dtype=int) # initialize an array
sortOwn(ar)
np.savetxt("sorted2.txt",ar[None], header="Own sort",fmt='%i')
