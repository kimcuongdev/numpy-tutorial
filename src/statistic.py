import numpy as np
#Min, Max
stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))
print(np.min(stats, axis= 1))
print(np.max(stats, axis = 1))
#Sum
print(np.sum(stats))
print(np.sum(stats,axis = 1))