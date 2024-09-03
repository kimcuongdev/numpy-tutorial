import numpy as np
#Boolean masking
arr = np.genfromtxt('data.txt', delimiter=',', dtype='int32')
print(arr)
print(arr > 25)
greater_than25 = arr[arr>25]    ##elements
print(greater_than25)
a = ((arr > 15) & (arr < 25)) ##boolean
print(a)
#Indexing with a list
a = np.array([1,2,3,4,5,6,7,8,9])
b = a[[1,2,-1]]
print(b)
#Is column has any elements > 25 ?
print(np.any(arr > 25, axis = 0))
#Is row has any elements > 25 ?
print(np.any(arr > 25, axis = 1))
#Is column has all elements > 25 ?
print(np.all(arr > 25, axis = 0))
#Is row has all elements > 25 ?
print(np.all(arr > 25, axis = 1))