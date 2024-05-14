
import numpy as np 

y1 = np.array([[5, 5, 1, 6, 5],
       [7, 7, 8, 9, 6],
       [1, 7, 2, 4, 5],
       [3, 4, 7, 0, 8],
       [1, 8, 2, 0, 2]])

# 1. Multipliez les lignes paires par 2
y1[::2, :] = y1[::2, :]*2

# 2. Multipliez les lignes impaires par 3
y1[1::2, :] = y1[1::2, :]*3

# 3. ajoutez 100 à la dernière valeur de chaque ligne
y1[:, -1] = y1[:, -1] + 100

y2 = np.array([[[89, 26, 78, 55, 23],
        [32, 92, 86, 55, 27],
        [87, 46, 63, 43, 77],
        [27, 18, 15, 20, 65],
        [52, 75, 82,  9, 38]],

       [[78, 20, 86, 16, 31],
        [46,  3, 59,  6, 50],
        [76, 73, 41, 66, 42],
        [70, 80, 62, 58, 41],
        [41, 65, 49,  0, 79]],

       [[13,  9, 58, 35, 32],
        [80, 86, 30, 73, 18],
        [52, 73, 74,  8, 40],
        [80, 27, 26, 94,  8],
        [30, 62,  3, 35, 75]],

       [[69, 54, 24, 28, 44],
        [29, 85, 56,  7, 69],
        [13,  1, 62, 10, 66],
        [ 6,  5, 31, 78, 92],
        [11, 41, 38,  4, 67]],

       [[30, 91, 12, 10, 91],
        [65, 95, 36, 54, 35],
        [49, 96, 21,  5, 87],
        [68, 82, 90, 36, 56],
        [41, 18, 75, 39, 99]]])

print( y1[0] )

# 4. chaque ligne paire et chaque ligne paire de chaque tableau on mulitplie par 2
y2[::2, ::2, :] = y2[::2, ::2, :]  * 2

# 5. Ajoutez 100 à chaque valeur de chaque tableau 5x5 de chaque ligne impaire du tableau y2

y2[1::2] = y2[1::2] + 100

"""
Reprenez la matrice initiale y2 et ajoutez 100 à la dernière valeur de chaque ligne de chaque matrice.
"""

y2[:, :, 2] =  y2[:, :, 2] + 1000