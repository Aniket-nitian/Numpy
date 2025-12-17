import numpy as np

#array modification
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)

#!insertion
arr_inserted = np.insert(arr, 2, 25,axis=None)  # Insert 25 at index 2
print("Array after Insertion:", arr_inserted)

#inser into 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_2d_inserted = np.insert(arr_2d, 1, [7, 8, 9], axis=0)  # Insert new row at index 1
print("2D Array after Insertion:\n", arr_2d_inserted)

#!Append
arr_appended = np.append(arr, [60, 70, 80])  # Append elements at the end
print("Array after Appending:", arr_appended)

#! concatenate
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_concatenated = np.concatenate((arr1, arr2))  # Concatenate two arrays
print("Concatenated Array:", arr_concatenated)

#!removal
arr_removed = np.delete(arr, 2)  # Remove element at index 2
print("Array after Removal:", arr_removed)
#remove from 2D array
arr_2d_removed = np.delete(arr_2d, 0, axis=0)  # Remove first row
print("2D Array after Removal:\n", arr_2d_removed)

#!stacking
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
arr_stacked = np.stack((arr_a, arr_b), axis=0)  # Stack arrays along a new axis
print("Stacked Array:\n", arr_stacked)
#horizontal stacking
arr_hstacked = np.hstack((arr_a, arr_b))  # Horizontal stacking
print("Horizontally Stacked Array:", arr_hstacked)  
#vertical stacking
arr_vstacked = np.vstack((arr_a, arr_b))  # Vertical stacking       
print("Vertically Stacked Array:\n", arr_vstacked)



#!splitting
arr_to_split = np.array([10, 20, 30, 40, 50, 60])
arr_split = np.array_split(arr_to_split, 3)  # Split array into 3 parts
print("Split Arrays:", arr_split)
#horizontal splitting
arr_2d_to_split = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_hsplit = np.hsplit(arr_2d_to_split, 2)  # Horizontal split into 2 parts
print("Horizontally Split Arrays:", arr_hsplit)

#vertical splitting
arr_vsplit = np.vsplit(arr_2d_to_split, 2)  # Vertical split into 2 parts
print("Vertically Split Arrays:", arr_vsplit) 
