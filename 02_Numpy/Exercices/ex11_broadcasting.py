import numpy as np 

DIM = 3

x = np.random.rand(DIM)

def matDiag(x):
    diag = np.zeros((DIM, DIM))

    for i in range(len(x)):
        diag[i, i] = x[i]

    return diag


print( matDiag(x) )