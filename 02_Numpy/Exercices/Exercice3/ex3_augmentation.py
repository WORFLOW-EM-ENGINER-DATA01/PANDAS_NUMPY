
import numpy as np 

a = np.array([82, 92, 89, 65, 77, 66, 69, 65, 79, 51])

rate = lambda x: x*1.1

print(np.where( a % 2 == 0, rate(a) , a))

print( rate( a[ a % 2 == 0] ) )