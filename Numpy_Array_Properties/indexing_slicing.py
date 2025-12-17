import numpy as np

#indexong nad slicing

arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
# Indexing
print("Element at index 0:", arr[0])
print("Element at index 2:", arr[2])
print("Element at index -1 (last element):", arr[-1])

# Slicing
print("Elements from index 1 to 3:", arr[1:4])
print("Elements from start to index 2:", arr[:3])
print("Elements from index 2 to end:", arr[2:])
print("Elements with step 2:", arr[::2])

#facy indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:\n", arr2d)  
# Fancy Indexing
rows = np.array([0, 2])
cols = np.array([1, 2])
fancy_indexed_elements = arr2d[rows, cols]  # Select elements at positions (0,1) and (2,2)
print("Fancy Indexed Elements:", fancy_indexed_elements)

# Boolean Indexing
bool_idx = arr2d > 5 # Get boolean array where condition is met, elements greater than 5
filtered_elements = arr2d[bool_idx]
print("Filtered Elements (greater than 5):", filtered_elements)
