
import numpy as np 

a = np.array([
    [13, 22, 28, 66, 40],
    [16, 59, 37, 33, 28],
    [34, 98, 54, 48, 96],
    [13, 84, 93, 79, 76],
    [63, 50, 12, 69, 12]
])

mins = a.min(1)
l, c = a.shape

posMinLine = []
for i in range(l):
    # le min de la première ligne
    minLine = mins[i]

    # On parcourir tous les éléments de la colonne
    # pour rechercher la position du min
    for j in range(c):
        if a[i,j] == minLine:
            posMinLine.append((minLine, i, j))

print(posMinLine)