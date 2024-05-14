import numpy as np

def circular(n):

    c = np.empty((n, n), dtype='int8')

    for i in range(n):
        c[i] = [ ( k + i  ) % n + 1 for k in range(n) ]

    return c

print(circular(10))