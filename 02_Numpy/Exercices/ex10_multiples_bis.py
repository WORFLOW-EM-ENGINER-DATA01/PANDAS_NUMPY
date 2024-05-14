import numpy as np 

DIM = 5
MAX_NUM = 50

dataset = np.random.randint(1, MAX_NUM, size=(DIM, DIM) )

print(dataset)

# 1. Générez une liste/array des multiples de 11 inférieurs à MAX_NUM
y = np.arange(11, 50, 11)

# print( np.isin(dataset, y) )
# sur les lignes
mask = np.any( np.isin(dataset, y), axis=1)
print(mask)

# 2. En utilisant np.isin(dataset, multiple11 ) trouvez tous les nombres multiples de 11 dans le dataset. Donnez le nombre de chaque multiple présent 
# Dans ce tableau

# print( dataset[ np.isin(dataset, y) ])

m = np.unique(dataset[ np.isin(dataset, y) ] )

u, count = np.unique( dataset[ np.isin(dataset, y) ], return_counts=True)

print( dict( zip(u, count)) )

# print(dataset)

# 3. Supprimez maintenant toutes les lignes du tableau ayant au moins un 0

# En utilisant le mask

# Négation sur les bits
mask = ~ mask
# sur chaque ligne on applique le mask
print(dataset[mask, :])

x = np.array([[1,2,3], [4,5,np.nan], [7,8,9]])

print(x)

print(np.isnan(x))
print(np.any(np.isnan(x), 1))
print(x[ ~np.any(np.isnan(x), 1) ])

mask = np.any (np.isnan(x), 0 )

xt = x.transpose()

print( (xt[ ~np.any( np.isnan(xt), 1 ) ]).transpose() )
