import numpy as np

# Q1
arr = np.array([1,2,3,4,5])
print(arr)
arr = arr + 2     
print(arr)   
arr = arr * 3
print(arr)   
arr = arr / 2
print(arr)  

#Q2 (a)
arr = np.array([1,2,3,6,4,5])
arr = arr[::-1]
print(arr)

#Q2(b)
x = np.array([1,2,3,4,5,1,2,1,1,1])
y = np.array([1,1,1,2,3,4,2,4,3,3])
unique_x, counts_x = np.unique(x, return_counts = True)
unique_y, counts_y = np.unique(y, return_counts = True)
most_frequent_x = unique_x[np.argmax(counts_x)]
most_frequent_y = unique_y[np.argmax(counts_y)]
index_x = np.where(x == most_frequent_x)[0]
index_y = np.where(y == most_frequent_y)[0]
print("Most frequent element in x:", most_frequent_x, "at index", index_x)
print("Most frequent element in y:", most_frequent_y, "at index", index_y)


#Q3
arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(arr[0][1])
print(arr[2][0])
#Q4
bhagya = np.linspace(10, 100, 25)
print(bhagya)
print("Dimensions:", bhagya.ndim)
print("Shape:", bhagya.shape)
print("Total elements:", bhagya.size)
print("Data type:", bhagya.dtype)
print("Total bytes:", bhagya.nbytes)
bhagya_transpose = bhagya.reshape(-1, 1)
print(bhagya_transpose)
bhagya_transpose = bhagya.T
print(bhagya_transpose)

#In this case, "T" was not able to change the array because it is 1-D array, but reshape was able to do so, and it became a column vector.

#Q5
ucs420_bhagya = np.array([[10,20,30,40], [50,60,70,80], [90,15,20,35]])
print(ucs420_bhagya)
print("Mean:", np.mean(ucs420_bhagya))
print("Median:", np.median(ucs420_bhagya))
print("Max value", np.max(ucs420_bhagya))
print("Min value", np.min(ucs420_bhagya))
print("Unique elements:", np.unique(ucs420_bhagya))
reshaped_ucs420_bhagya = ucs420_bhagya.reshape(4,3)
resized_ucs420_bhagya = np.resize(ucs420_bhagya, (2,3))
print(reshaped_ucs420_bhagya)
print(resized_ucs420_bhagya)