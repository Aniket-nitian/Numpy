import numpy as np

#reshaping and manipulating arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)
# Reshaping
reshaped_arr = arr.reshape((3, 2))
print("Reshaped Array (3x2):\n", reshaped_arr)

# Flattening `(returns a copy of the array collapsed into one dimension)`
flattened_arr = arr.flatten()
print("Flattened Array:", flattened_arr)

# Ravel (returns a flattened array, but as a view if possible)
raveled_arr = arr.ravel()
print("Raveled Array:", raveled_arr)

