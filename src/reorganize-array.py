import numpy as np
#Reshape
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((8,1))
print(after)
after = before.reshape((2,2,2))
print(after)
#Vertically stacking vectors (must have same length)
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v1,v2]))
#Horizontially stacking vectors
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
print(np.hstack([h1,h2]))