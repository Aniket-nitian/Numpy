import numpy as np

# Basic mathematical operations

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])
# Addition
add_result = arr1 + arr2
print("Addition Result:", add_result)

#aggregate functions
sum_result = np.sum(arr1)
print("Sum Result:", sum_result)
mean_result = np.mean(arr1)
print("Mean Result:", mean_result)
max_result = np.max(arr1)
print("Max Result:", max_result)
min_result = np.min(arr1)
print("Min Result:", min_result)
std_result = np.std(arr1)
print("Standard Deviation Result:", std_result)
var_result = np.var(arr1)
print("Variance Result:", var_result)