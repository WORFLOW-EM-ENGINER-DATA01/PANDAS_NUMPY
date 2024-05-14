import numpy as np
import os

file_path = os.path.join(os.path.dirname( __file__ ), './sources/pollution_2016.csv')

with open(file_path, 'r') as f:
    dataset = np.loadtxt(f, delimiter=',', skiprows=1, dtype={'names': ('country', 'prct_rpt_pollution'),
                         'formats': ('U29',  'f4')} )

t = len(dataset)
print(dataset)
dataset = np.sort(dataset, order='prct_rpt_pollution')

# Max pollution
country, percentage = dataset[-1]
print("Country : {}, percentage : {}".format(country, percentage) )