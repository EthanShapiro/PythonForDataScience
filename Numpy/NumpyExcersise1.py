# Import numpy as np
import numpy as np

# Create an array of 10 zeros
print(np.zeros((1, 10)))

# Create an array of 10 fives
print(np.array([5]*10))

# Create an array of integers from 10 to 50
print(np.arange(10, 51))

# Create a 3x3 matrix with values 0-8
arr = np.arange(0, 9)
print(arr.reshape((3, 3)))

# Create a 3x3 identity matrix
print(np.eye(3, 3))

# Use NumPy to generate a random number between 0 and 1
print(np.random.random(1))

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
print(np.random.randn(5, 5))

# Create a matrix from 0-1 by 0.01 increments
print(np.arange(0.01, 1.01, 0.01).reshape(10, 10))

# Create an array of 20 linearly spaced points between 0 and 1
print(np.linspace(0, 1))

mat = np.arange(1,26).reshape(5,5)
print(mat)
mat = np.arange(11, 26).reshape(3, 5)
print(mat[:, 1:])
print(mat[1, 4])
print(np.arange(2, 16, 5))
print(np.arange(21, 26))
print(np.arange(16, 26).reshape(2, 5))
print(mat.sum())

