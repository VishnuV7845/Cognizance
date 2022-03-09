import numpy as np

print("This program generates two random arrays and checks if they are equal or not.")

arr1 = np.random.randint(0, 2, 6)
print("Array 1:", arr1)

arr2 = np.random.randint(0, 2, 6)
print("Array 2:", arr2)

out = np.allclose(arr1, arr2)
print(out)