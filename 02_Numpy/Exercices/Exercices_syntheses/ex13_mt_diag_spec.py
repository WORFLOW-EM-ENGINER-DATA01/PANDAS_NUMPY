import numpy as np

def createMatTriDiag(n):
    m = np.zeros( (n, n), dtype = 'float64' )

    for i in range(n):
        m[i,i] = 1
        if i > 0:
            m[i, i - 1] = 1
        if i < n - 1:
            m[i, i+1] = 1
        

    return m

print( createMatTriDiag(10) )

def specialMatrix(n):
    m = np.zeros( (n, n), dtype = 'float64' )
    for i in range(n):
        num = i + 1
        for j in range(n):
            if i == j:
                num = 1
            m[i, j] = num
            num += 1

    return m

print(specialMatrix(4))
