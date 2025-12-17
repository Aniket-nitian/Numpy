import numpy as np

#shape size type
arr = np.array([1, 2, 3, 4, 5])
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Type:", arr.dtype)

#2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Shape:", arr_2d.shape)
print("2D Size:", arr_2d.size)
print("2D Type:", arr_2d.dtype)
print("2D Type:", arr_2d.ndim)

#type conversion
arr_float = arr.astype(np.float64)
print("Converted Type:", arr_float.dtype) 

float_arr = np.array([1.5, 2.5, 3.5])
print("Original Type:", float_arr.dtype)
int_arr = float_arr.astype(np.int32) 
print("Converted Type:", int_arr.dtype)

