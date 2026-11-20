# 18/9/26

import numpy as np
from scipy import sparse

vector_row = np.array([1,2,3])
print(vector_row)
print()

vector_column = np.array([[1],[2],[3]])
print(vector_column[0][0])
print(vector_column[0,0])
print(vector_column[2,0])
print()


matrix = np.array([[1,2],
                   [1,2],
                   [1,2]
                   ])
print(matrix)
print()

matrix_s = sparse.csr_matrix(matrix)
print(matrix_s)


l1 = [1,2,3,4]
l2 = [[1,2,3,4]]
l3 = [
      [1,2,3,4],
      [10,20,30,40],
      [100,200,300,400]  
     ]

print(l1)
print(l2)
print(l3)
print()


a1 = np.array(l1)
print(a1)
a2 = np.array(l2)
print(a2)
a3 = np.array(l3)
print(a3)

print("Shape func")
print(a1.shape) # 1 dimensional array with 4 elements
print(a2.shape) # 2 dimensional with 1 nested array with 4 elements
print(a3.shape) # 2 dimensional array with 3 nested array and 4 elemens each

# creating array from scratch with np function
print("linscape func")
a4 = np.linspace(0,10,5) # give us 5 elements form 0-10(inclusive) that are evenly spaced
print(a4)


print("Slicing")
a5 = np.array([['a','b','c'],
              ['d','e','f']])
print(a5)
print(a5[1,2])

a6= np.array([[1,2,3,4,5],[10,20,30,40,50],[6,7,8,9,10]])
print(a6)
print([a6[0][2:4]])
print([a6[1, 2:4]])
print(a6[0:2,2:4])
print(a6[1:,3:])
print()

print("Sum func")
a7 = np.array([[1,2,3,4],
               [5,6,7,8]])
print(a7.sum())
print(a7.sum(axis=0)) # axis 0 for columns
print(a7.sum(axis=1)) # axis 1 for rows
print()

print("Reshape func")
a8 = np.array([1,2,3,4,5,6,7,8])
print(a8.reshape(4,2))
print(a8.reshape(2,4))
print("To one-dimensional: ",a8.reshape(-1))
print()

# 21/9/26

arr = np.array([[1,2,3,4], 
                [5,6,7,8]
                ])

print(arr.reshape(4, -1)) # when you are sure you want 2 rows but dont know the num of columns to specify put -1

print("Concatenate")
arr9 = np.array([[1,2], [3,4], [5,6]])
arr10 = np.array([[7,8]])

arr11 = np.concatenate((arr9, arr10)) # concatenate using column, axis = 0 by default
print(arr11)

arr12 = np.array([[9], [10], [11], [12]])
print(arr12)

arr13 = np.concatenate((arr12, arr11), axis=1) # concatenate using rows (axis = 0 by default (using col))
print(arr13)

print(dir(np.array))

arr14=np.array([1,2,3,4,5,6])
print(arr14)

r1=arr14.reshape(2,-1) # using reshape direct function
print(r1)

pr2=np.reshape(arr14, (2,-1)) # using wrapper func "reshape" from np module that calls the member method on the arr14 object

