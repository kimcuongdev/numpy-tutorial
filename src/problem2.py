import  numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print(arr)
#Blue
print(arr[2:4,0:2])
#Green
print(arr[[0,1,2,3],[1,2,3,4]])
#Red
print(arr[[0,4,5],3:5])