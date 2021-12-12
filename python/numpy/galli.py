import numpy as np
from numpy.core.fromnumeric import shape


#BASIC INFO
'''
#2d array
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype = 'int16') #by default int 32
print(mat)

#get dimension
print(mat.ndim)

#get shape
print(mat.shape)

#get type
print(mat.dtype)

#get number of bytes
print(mat.itemsize)

#get number of items
print(mat.size)

#get total size
print(mat.nbytes) #mat.itemsize * mat.size
'''


#INDEXING
'''
mat = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

#get specific element
print(mat[1, 3]) #array[row, column]
print(mat[1, -2])

#get specific row
print(mat[0, :])

#get specific column
print(mat[:, 3])

#with step size
print(mat[0, ::2])
print(mat[2, 1::2])
print(mat[1, ::-2])

#change element
mat[1, 4] = 0
print(mat) 

#change rows
mat[1, :] = [6, 7, 8, 9, 10]
print(mat)

#3d arrays
d3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print(d3)

#accessing specific element in 3d array
print(d3[2, 0, 1])
'''


#INITIALIZING DIFFERENT ARRAYS
'''
#all 0s matrix
zeros = np.zeros((4, 3))
print(zeros)

#all 1s matrix
ones = np.ones((4, 3))
print(ones)

#all any other number
any = np.full((4, 3), 27)
print(any)

#full like
cop = np.full_like(any, 4)
print(cop)

#random number matrix
rand = np.random.rand(4, 3)
print(rand)

#random number copy shape
rand_ = np.random.random_sample(rand.shape)
print(rand_)

#random integers
ints = np.random.randint(10, 100, size = (4, 3))
print(ints)

#identity matrix
print(np.identity(4))

#repeat array x times
new = np.array([[1, 2, 3]])
print(np.repeat(new, 3, axis = 0))

#copying arrays
a = np.array([1, 2, 3])
b = a.copy()
b[1] = 100
print(a, b)
'''


#Question: 1, 1, 1, 1, 1
#          1, 0, 0, 0, 1
#          1, 0, 9, 0, 1
#          1, 0, 0, 0, 1
#          1, 1, 1, 1, 1 
'''
final = np.ones((5, 5))
final[1:4, 1:4] = np.zeros((3, 3))
final[2, 2] = 9
print(final)
'''


#MATHS
'''
#basic maths
a = np.array([1, 2, 3])
print(a)
print(a+2)
print(a-2)
print(a*2)
print(a/2)
print(a**2)
b = np.array([3, 2, 1])
print(a+b)
print(np.sin(a))
print(np.cos(a))

#basic linear algebra multiplication
a = np.full((3, 2), 2)
b = np.full((2, 3), 5)
print(np.matmul(a, b))

#find determinant
c = np.identity(3)
print(np.linalg.det(c))

#https://numpy.org/doc/stable/reference/routines.linalg.html
'''


#STATISTICS
'''
stats = np.array([[1, 2, 4], [6, 5, 3]])
print(np.min(stats))
print(np.max(stats))
print(np.sum(stats))
print(np.mean(stats))
'''


#REORGANIZING ARRAYS
'''
#reshaping
bef = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
aft = bef.reshape(3, 4)
print(bef)
print(aft)

#horizontal and vertically stacking
v1 = np.array([[1, 2, 3, 4], [9, 10, 11, 12]])
v2 = np.array([[5, 6, 7, 8], [13, 14, 15, 16]])
print(np.vstack([v1, v2]))
print(np.vstack([v1[0], v2[0], v1[1], v2[1]]))
print(np.hstack([v1, v2]))
print()
'''


#MISCELLANEOUS
'''
#loading data from file
data = np.genfromtxt('data.txt', delimiter = ',')
print(data.astype('int32'))

#boolean masking and advanced indexing
print(data > 50)
print(data[data > 50])
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.any(7 not in a[a%2==1], axis = 0))

#question: print odd numbers
print(a[((a % 2 == 1) & (a != 7))])
'''