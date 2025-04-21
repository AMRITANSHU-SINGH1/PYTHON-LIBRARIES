import numpy as np
arr=np.array([1,2,3])
x=arr.copy()
arr[0]=42
print(arr)
print(x)


y=arr.view()
print(y)
arr[1]=37
print(arr)
print(y)


#Check if Array Owns its Data
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()

print(x.base)
print(y.base)
