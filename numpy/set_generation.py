import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(1,100, 100)

# a = 1
# b = 1
# c = 50


# s = np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)


# plt.plot(x,s)
# plt.show()


a = 1
b = 1
c = 60
d = 90

s = np.minimum(np.maximum(np.minimum((x-a)/(b-a), (d-x)/(d-c)), 0), 1)


print(x[75], s[75])

# plt.plot(x,s)
# plt.show()

print(np.abs(x-76).argmin())