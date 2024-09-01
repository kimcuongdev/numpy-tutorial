import numpy as np
a = np.array([1,2,3])
a1 = np.array([1,2,3], dtype='int16') #specifi
print(a)
b = np.array([[9.0,8.0,7.0],[5.0,4.0,3.0]])
print(b)

#Get Dimension
print(a.ndim)  #1

#Get Shape
print(a.shape) #(3,)
print(b.shape) #(2,3)

#Get Type
print(a.dtype) #int64
print(a1.dtype) #int16

#Get Size
print(a.itemsize) #int64 = 8bytes
print(a1.itemsize) #int16 = 2bytes
print(b.itemsize) #8bytes

#Get total size
print(a.size)     # 3 elements
print(a.nbytes)   # 24bytes = 3(size) * 8(itemsize)