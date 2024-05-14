
import numpy as np 

dt = np.dtype([('name', np.dtype('U25')), ('grades', np.float64 )]) 

# x is a structured array with names and marks of students. 
# Data type of name of the student is np.unicode_ and 
# data type of marks is np.float(64) 
dataset = np.array([
      ("Luce du Coulon" , 18.5),
      ("Auguste Dupont", 2.5),
      ("Roger Le Voisi", 8.5),
      ("Alexandre Lacri", 10.5),
      ("Jacques Humber", 22.7),
      ("Thérèse Guille", 17.8),
      ("Gilles Gros-Bodin", 23.7),
      ("Amélie Pires", 10.6),
      ("Marcel Laporte", 11.6),
      ("Geneviève Marchal", 8.15),
], 
    dtype=dt
) 

