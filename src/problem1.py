import  numpy as np
out = np.ones((5,5),dtype='int32')
in_matrix = np.zeros((3,3),dtype='int32')
in_matrix[1,1] = 9
out[1:4,1:4] = in_matrix
print(out)