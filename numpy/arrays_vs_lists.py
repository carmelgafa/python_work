import numpy as np

# python lists
L=[1,2,3]
L.append(4)
L = L+[5]
for e in L:
    print(e)

# numpy array. no easy way to append
A = np.array([1,2,3])
for e in A:
    print(e)

# vector addition
L2 = []
for e in L:
    L2.append(e+e)

for e in L2:
    print(e)

# use + to vector addion in numpy
A2 = A+A
# scalar multiplication
A2 = 2 * A2
# square
A2 = A**2

for e in A2:
    print(e)


