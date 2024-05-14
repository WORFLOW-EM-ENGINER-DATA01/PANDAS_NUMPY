import numpy as np 
import math as m

january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5, 7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2])

print(january > 0)
print(january[ january > 0 ])   

days_january = np.arange(1, january.size + 1, dtype=np.int8)

# Comparaison est-ce qu'il y a plus de température positive que négative
(january > 0).sum() > (january < 0).sum()

# Moyenne des températures sur le mois de Janvier
# np.sum(january > 0)
print( m = (january > 0).sum() / 31)

print( round( january[ january > 0 ].sum() / 31, 1) )

# Remplacez les températures < 0 par la température moyenne

averageNegative = np.mean(january[ january > 0 ])

january[ january < 0 ] = averageNegative

