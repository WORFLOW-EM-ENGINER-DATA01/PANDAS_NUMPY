import os
import numpy as np

# Lecture du fichier
file_path = os.path.join(os.path.dirname(__file__), './sources/input.txt')
read_data = None

with open(file_path, 'r') as f:
    read_data = np.loadtxt(f, dtype='str')

# On crée une fonction pour compter le nombre d'occurence d'un symbole
def parser(row, pattern = 'X'):

    if not row:
        pass
    
    return row.count(pattern)

read_data = read_data[:, np.newaxis]
print(read_data.shape)

dt = np.dtype([
    ('pattern', np.dtype('U29')), ('count', np.int8) 
])

dataset = np.zeros( 30, dtype = dt)

for i, row in enumerate(read_data):
    dataset[i] = (row[0], parser(row[0]))

dataset = np.sort( dataset, order='count')
print(dataset)