# import numpy as ap

# # print(arr)
# # print(type(arr))


# # mylist=[1,2,3,4]
# # print(mylist)

# # print(ap.__version__)
# arr0=ap.array(42)
# print(arr0)
# arr1=ap.array((1,2,3,4,5))
# print(arr1)
# arr2=ap.array([[1,2,3],[22,34,23342]]) # an 2 dimensional array
# print(arr2)

# arr3=ap.array([[[1,2,3],[4,5,7]],[[2,24,342],[384,34,234]]]) # an 3d array

# print(arr0.ndim)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

import numpy as np
arr=np.array([1,2,3,4,5],ndmin=50)
print(arr)
print('number of dimensions:',arr.ndim)