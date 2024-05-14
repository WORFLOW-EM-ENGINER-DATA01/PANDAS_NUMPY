
import numpy as np 

students = np.array([
    [  "Name: Luce du Coulon" , "phone: 201-20-30"],
    [  "Name: Auguste Dupont", "phone: 201-22-30"],
    [  "Name: Roger Le Voisi", "phone: 201-27-30"],
    [  "Name: Alexandre Lacri", "phone: 201-10-30"],
    [  "Name: Jacques Humber", "phone: 201-20-35"],
    [  "Name: Thérèse Guille", "phone: 201-20-38"],
    [  "Name: Gilles Gros-Bodin", "phone: 201-20-39"],
    [  "Name: Amélie Pires", "phone: 201-25-39"],
    [  "Name: Marcel Laporte", "phone: 201-20-39"],
    [  "Name: Geneviève Marchal", "phone: 301-20-39"] 
])

# for i, line in enumerate( students ):
#     for j, column in enumerate(line):
#         students[i,j] = column[len('Name:'):].strip() if "Name:" in column else column[len('phone:'):].strip() 


sanitize = np.array([
    [ [ c[6:].strip() for c in l ]  for l in students ]
])

print(sanitize)

# indexation avancée
mask = np.array( [ [ '-30' in c for c in l ] for l in students ] )
print(students[mask])