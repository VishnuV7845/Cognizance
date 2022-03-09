#Convert the data type of a given array using this program.
import numpy as np

arr = np.array([1.8, 0.3, 7.8, 4.5])
print("Array:", arr)
print("The type of this array is", arr.dtype)

arr = arr.astype(np.int64)
print("\nThe array type is changed using 'arr = arr.astype(np.int64), so the type of the array now is", arr.dtype)
print("The converted array is:", arr)