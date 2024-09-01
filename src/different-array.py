import numpy as np
#All 0s matrix
a = np.zeros(5)
print(a)
b = np.zeros((2,3))
print(b)
#All 1s matrix
c = np.ones((2,2,2))
print(c)
d = np.ones((2,2,3), dtype='int32')
print(d)
#All any other number
e = np.full((4,5),9,dtype='float32')
print(e)
#Any other number (full_like)
g = np.array([[1,2,3],[4,5,6]])
h = np.full_like(g,3)
print(h)
#Random decimal numbers
i = np.random.rand(1,2)
print(i)
k = np.random.random_sample(g.shape)
print(k)
#Random int numbers
l = np.random.randint(4, size = (3,3))
print(l)
#Random int numbers in range [a,b)
m = np.random.randint(-2,5, size = (1,3))
print(m)
#Identity matrix (ma tran don vi)
n = np.identity(4)
print(n)
#Repeat an array
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3]])
r_arr1 = np.repeat(arr1,3)
print(r_arr1)
r_arr2 = np.repeat(arr2,3, axis=0)
print(r_arr2)