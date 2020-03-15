import numpy as np

ar = np.array([79, 2, 150, 19, 15],dtype=int) # initialize an array

ar.sort() # sort with in-built function
np.savetxt("sorted1.txt",ar[None], header="In-built sort",fmt='%i')