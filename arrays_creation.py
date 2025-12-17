import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50 ])
print(arr_1d)
print(type(arr_1d))
print("")

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
print(type(arr_2d))
print("")

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)
print(type(arr_3d))
print("")

#multi-dimensional array
#matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix) 

#default value
zeros_array = np.zeros((2, 3))
print(zeros_array)

ones_array = np.ones((3, 2))
print(ones_array)

#full function
full_array = np.full((2, 4), 7)
print(full_array)

#creating sequence of numbers
arange_array = np.arange(0, 10, 2)
print(arange_array)

#identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)