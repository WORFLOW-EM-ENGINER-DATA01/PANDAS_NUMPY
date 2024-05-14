import numpy as np 

a = np.array([[1,2,8], [7,4,2], [9,1,7], [0,1,5], [6,4,3]])
x = np.array([1,2,3])

np.sqrt( ( (x-a)**2 ).sum(1) )
