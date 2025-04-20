#data types 
#use dtype 
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)    #output int64

arr2 = np.array(['apple', 'banana', 'cherry'])

print(arr2.dtype) #output <U6
'''Breakdown of <U6:
<: Indicates byte order (endianness). < means little-endian (common on most systems). For strings, it's not that important.

U: Stands for Unicode string.

6: Maximum number of Unicode characters per string'''
'''A Unicode string is a string that can store
 any character from almost any language or symbol system in
   the world — not just English letters!

'''

#so when i will do 
arr = np.array(['apple', 'banana', 'cherry',"watermelon"])

print(arr.dtype) #output is <U10 as because there is watermelon with len 10

#Creating Arrays With a Defined Data Type

arr=np.array([1,2,3,4],dtype='S')
print(arr) #output [b'1' b'2' b'3' b'4']
print(arr.dtype) # |S1

"|S1 means - Each element is a byte string, with up to 1 byte of data."
""" 'A' (Unicode) = character 'A'

b'A' (Bytes) = byte representing the ASCII value of 'A' → 65 in decimal """

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr) #output [1 2 3 4]
print(arr.dtype) #output


'''
Using dtype='i4' ensures:

Each element uses exactly 4 bytes of memory.

The array has consistent, efficient storage — useful for large arrays.


 Extra Tip: Size comparison

dtype	     Meaning	Size	Range
'i1'	int8	     1 byte	–128 to 127
'i2'	int16	2 bytes	–32,768 to 32,767
'i4'	int32	4 bytes	–2,147,483,648 to 2,147,483,647
'i8'	int64	8 bytes	~±9 quintillion
'''


#What if a Value Can Not Be Converted?
#If a type is given in which elements can't be casted then NumPy will raise a ValueError.