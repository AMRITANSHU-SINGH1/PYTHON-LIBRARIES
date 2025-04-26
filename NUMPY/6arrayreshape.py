import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape((1,4,3))
#meaning The outermost dimension will have 4 arrays, each with 3 elements:
print(arr)
print(newarr)
print(newarr.ndim)


# Reshape From 1-D to 3-D
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape((2,3,2))
print(newarr)