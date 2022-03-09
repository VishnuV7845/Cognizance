#Builds new vector from the given vector, which would contain five consecutive '0s' between each number.
import numpy as np

v1 = np.array([10, 11, 12, 13, 14])
print("Given vector:", v1)

n = 5
v2 = np.zeros(len(v1) + (len(v1)-1)*(n))
v2[::n+1] = v1

print("New vector:", v2)