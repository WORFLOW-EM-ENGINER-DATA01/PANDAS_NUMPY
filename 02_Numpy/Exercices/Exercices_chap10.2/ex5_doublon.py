
import numpy as np 

a = np.array([
    ["aaabbfffhjik", "hhhkkkiooo", "hhjuuk"],
    ["rrrtttyyuuii", "rroooiiiuuu", "jjjhhhaa"],
    ["aaabbgghhh", "iiikkkooomml", "hhhiijjjuu"],
    ["hhhyyytttuu", "xxxnnnooii", "kkkjjjuuppp"],
    ["qqqfffgghhh", "qqqkkklll", "ooohhhjjj"],
])

l, c = a.shape

sanitize = np.empty((l, c), dtype='<U12')

for i in range(l):
    for j in range(c):
        sanitize[i, j] = "".join( set(a[i, j]) )

print(sanitize)