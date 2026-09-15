import numpy as np
#Q1
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])
temperature += 2
print(temperature)
temp_fahrenheit = (temperature * 9/5) + 32
print(temp_fahrenheit)
print(temperature[temperature > 32])
count = np.sum(temperature > 32)
print("Count of temperatures above 32:",count)

# Vectorization helps us in performing operations on entire array without using for loops, in the case of list we will need a for loop to iterate over it and do operations
#Boolean indexing helps us in filtering the array based on condition and helps us in selecting specific elements easily


#Q2
steps = np.array([ [5000, 6200, 7100], [8000, 7500, 9000], [4500, 5100, 4800], [9000, 8500, 9500]])
print("Total steps:", np.sum(steps))
print("Mean of steps:", np.mean(steps))
print("Max value : ", np.max(steps), "Min value: ", np.min(steps))
print("Total steps for each day:", np.sum(steps, axis = 0))
print("Total steps for each user:", np.sum(steps, axis = 1))
print("Position of maximum steps:", np.unravel_index(np.argmax(steps), steps.shape))

# Q3
original = np.array([1,2,3,4,5,6])
subset = original[1:5]
subset[0] = 999
print("Original array:", original)
print("Subset array:", subset)
copied = original[1:5].copy()
copied[0] = 500
print("Original array:", original)
print("Copied array:", copied)
arr = np.arange(1, 13)
arr = arr.reshape(3, 4)
print(arr)
print("First row:", arr[0])
print("Last row:", arr[-1])
print("Second column:", arr[:, 1])
print("Elements from row 1-2 and column 2-3:", arr[0:2, 1:3])

flattened = arr.flatten()
raveled = arr.ravel()
print("Using flatten():", flattened)
print("Using ravel():", raveled)

raveled[0] = 1000
print("After modification, raveled array:", raveled)
print("Original", arr)

flattened[1] = 2000
print("After modifying flatten, flattened array:", flattened)
print("Properties:\n")
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("Data type:", arr.dtype)


#Q4
X = np.array([
    [6,70,3],
    [5,50,6],
    [8,80,2],
    [4,30,8]
])
y = np.array([40,65,30,85])
print("Shape:", X.shape)
print("Dimensions:", X.ndim)
X_transpose = X.T
print("Transpose:", X_transpose)
print("Rows of X represents users, columns represent features. In X_transpose, rows represent features and columns represent users.")

XtX = X.T @ X
print("X.T @ X:", XtX)
inverse = np.linalg.inv(XtX)
print("Inverse of X.T @ X:", inverse)

beta = np.linalg.inv(X.T @ X) @ X.T @ y
print("coefficients:", beta)

print("Sleep coefficient:", beta[0])
print("Activity coefficient:", beta[1])
print("Stress coefficient:", beta[2])

new_user = np.array([5,40,7])
predicted_score = new_user @ beta
print("New user:", new_user)
print("Predicted score:", predicted_score)
