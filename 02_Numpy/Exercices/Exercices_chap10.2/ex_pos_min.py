
import numpy as np 

a = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 13, 69, 12]
])

# On récupère dynamiquement les dimensions
l, c = a.shape

dt = np.dtype([
    ('min', np.dtype('int8')), ('pos', np.dtype('int8') ) 
])

dataset = np.empty( l , dtype = dt)

for i in range(l):
    m = a[i].min()
    for j in range(c):
        if a[i, j] == m:
            dataset[i] = (m, j)

print(dataset)

# Autre solution avec np.where

dataset = np.empty( l , dtype = dt)

for i in range(l):
    m = a[i].min()
    pos, = np.where( a[i] == m )
    if pos.size > 0:
        dataset[i] = (m, pos[0])

print(dataset)