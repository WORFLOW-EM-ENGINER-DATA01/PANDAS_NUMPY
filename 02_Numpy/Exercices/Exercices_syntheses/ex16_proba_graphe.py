# Matrice A matrice de transition

"""
Créer une fonction Pn qui donne l'état probabiliste au bout de n semaines

"""

import numpy as np

a = np.array([
    [ 0.333, 0.333, 0.333 ],
    [ 0., 0.5, 0.5 ],
    [ 0., 0., 1 ],
])

def P(v, m = a):
    c1, = v.shape
    c2, l2 = m.shape

    try:
        if c1 != l2:
             raise Exception('colonnes et lignes non conforment format : {} {}'.format(c2, l2) )

        return v @ m
    
    except ValueError:
       print("Oops!  That was no valid dim for your vector v.  Try again...")


# Calculez la valeur du vecteur initial

"""
C'est évident car 1/100 est malade patient 0 donc on a la matrice v ci-dessous
"""

v = np.array([0.99, 0, 0.01])

# Vérifiez que Pn = P0*A^n en le vérifiant pour les valeurs suivantes n = [1,2,3,4,5,6]

print(P(v, a))

print( v @ np.linalg.matrix_power(a, 4) )

print(  P( P( P( P(v) ) ) ) )

# Quelle est la probabilité qu'un individu soit sain au bout de 4 semaines ?

p4 = v @ np.linalg.matrix_power(a, 4)
pS, pI, pM = p4

print("Probabilité qu'un individu soit sain au bout de 4 semaines : {}".format(round( pS, 2) ))

# On vaccine la population au bout de la 4 eme semaine on a alors la matrice suivante 

b =  np.array([
    [ 5/12, 1/4, 1/3 ],
    [ 5/12, 1/4, 1/3 ],
    [ 1/6, 1/2, 1/3 ],
])

# Exprimez sous forme vectoriser pour n = 5 Q(n+1), S(n+1), I(n+1), M(n+1) en fonction de Sn, In et Mn
# On remarque que P4 = Q0
# Créez une fonction permettant de cacluler les probabilités pour les semaines suivantes, que pouvez-vous en déduire ?

n = 5
p = P(p4, b)
print(p)
s5 = 5/12 * p[0] + 5/12 * p[1] + 1/6 * p[2] 
i5 = 1/4 * p[0] + 1/4 * p[1] + 1/2 * p[2] 
m5 = 1/3 * p[0] + 1/3 * p[1] + 1/3 * p[2] 
print(s5, i5, m5)

# Créez une fonction qui permet de calculer les probabilités suivantes 
def pNextWeek(n):
    p = p4
    for _ in range(n):
        p = P(p, b)
        print(p)

    s = 5/12 * p[0] + 5/12 * p[1] + 1/6 * p[2] 
    i = 1/4 * p[0] + 1/4 * p[1] + 1/2 * p[2] 
    m = 1/3 * p[0] + 1/3 * p[1] + 1/3 * p[2] 

    return s, i, m

# la population des malades reste constante on ne peut donc pas espérer éradiquer la maladie.
print(pNextWeek(10))