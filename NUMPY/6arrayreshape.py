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

# is arr.reshape is view or copy of the original array ???

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

u=arr.reshape(4,2)
print(u)            
print(u.base)  # answer is it is just a view of the original array 
# as the output is [1,2,3,4,5,6,7,8]


# important thing to notice 
'''changes  made to view also affect original array'''

exapl=np.array([1,2,3,4,5,6,7,8])
view=exapl.reshape(2,4)

view[0][0]=100

print('view array:',view)
print('origianl:',exapl)
