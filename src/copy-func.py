import numpy as np
a1 = np.array([1,2,3])
b1 = a1
b1[0] = 100
print(b1)
print(a1)
a2 = np.array([1,2,3])
b2 = a2.copy()
b2[0] = 100
print(a2)
print(b2)