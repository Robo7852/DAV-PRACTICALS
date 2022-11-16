# 2. Write programs in Python using NumPy library to do the following:

# a. Compute the mean, standard deviation, and variance of a two dimensional random integer array
# along the second axis.
import numpy as np
print("Question 1:")
x = np.random.randint(1, 10, (2, 2))
print("Original array:")
print(x)

print("Mean of each column:")
print(x.mean(axis=1))

print("Standard deviation of each column:")
print(x.std(axis=1))

print("Variance of each column:")
print(x.var(axis=1))


# b. Get the indices of the sorted elements of a given array.
#     a. B = [56, 48, 22, 41, 78, 91, 24, 46, 8, 33]
print("\nQuestion 2:")
B = [56, 48, 22, 41, 78, 91, 24, 46, 8, 33]
print("Sorted array:", np.sort(B))
print("Sorted indices:", np.argsort(B))

# c. Create a 2-dimensional array of size m x n integer elements, also print the shape, type and data
# type of the array and then reshape it into nx m array, n and m are user inputs given at the run time.
print("\nQuestion 3:")
arr2D = np.random.randint(1, 10, size=(2, 3))
# arr2D=np.array([[1,2,3],[4,5,6]])
print("Original array:\n", arr2D)
print("Shape:", arr2D.shape)
print("Type:", type(arr2D))
print("Data type:", arr2D.dtype)

n = int(input("Enter value of m: "))
m = int(input("Enter value of n: "))
while n*m != arr2D.shape[0]*arr2D.shape[1]:
    # check if product is equal to number of elements in array
    print("Product must be", arr2D.shape[0]*arr2D.shape[1], "to reshape")
    n = int(input("Enter value of m: "))
    m = int(input("Enter value of n: "))
print("Reshaped array:\n", arr2D.reshape(n, m))

# d. Test whether the elements of a given array are zero, non-zero and NaN. Record the indices of
# these elements in three separate arrays.
print("\nQuestion 4:")
arr = np.array([-3, -9, 0, 1, np.nan, 1, 0, 0, np.nan])
print("Original array:", arr)
print("Zeros:", np.where(arr == 0))
print("Non-Zeros:", np.where(arr != 0))  # nan is considered as non zero
print("NaN:", np.where(np.isnan(arr)))
