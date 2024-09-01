import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#Get a specific element [r,c] [hang,cot]
#index starts with 0
print(a[1][2]) #10
print(a[1,2])

#Get a specific row
#example with row 0 [1,2,3,...]
print(a[0,:])
#example with row 1 [8,9,10,...]
print(a[1,:])

#Get a specific column
#example with column 5 [6,13]
print(a[:,5])

#[startIndex:endIndex:stepSize]
#print out [startIndex,endIndex) with stepSize
#example with a[0][1] (2) to a[0][4] (5) with step = 2
print(a[0,1:5:2])  #[2,4]
print(a[0,1:6:2])  #[2,4,6]
#example with negative index
print(a[1, 1:-1:2])

#Changing
#Change a[1,5] to 20
a[1,5] = 20        #[1][5] same
print(a)
#Change a column
a[:,2] = 5
a[:,5] = [15, 16]
print(a)

#3D example
#Access
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
'''
     C0     C1
R0  [1,2] [3,4]
R1  [5,6] [7,8]
'''
print(c[1,0,0]) #5
print(c[0,:,:])
print(c[:,1,:])
print(c[:,:,1])
#Change
c[1,1,1] = 9
print(c)
c[0,0,:] = [11,22]
print(c)
c[:,1,:] = [[33,44],[77,88]]
print(c)