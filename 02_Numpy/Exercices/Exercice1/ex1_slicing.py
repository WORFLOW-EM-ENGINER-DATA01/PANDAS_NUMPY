
import numpy as np 

x1 = np.array([[9, 1, 2],
    [8, 0, 2],
    [5, 1, 5]])

# première ligne
x1[0,:]

# deuxième colonne
x1[:,0]

# somme lignes et colonnes
print( x1.sum(0) )
print( x1.sum(1) )

# Destructuration somme des colonnes
(c1, c2, c3) = x1.sum(0)

# Destructuration somme des lignes
(l1, l2, l3) = x1.sum(0)

# Dimension 2x2x2
x2 = np.array([ 
    [ [8, 4],[8, 9] ],
    [ [3, 0],[5, 0] ] 
])

# somme axis
print(x2.sum(0))
print(x2.sum(1))
print(x2.sum(2))

x3 = x2.sum(2).sum(1)

# Sélection

x2[:, :, -1]

"""
array([[4, 9],
       [0, 0]])

"""