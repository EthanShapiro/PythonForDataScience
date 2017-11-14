import numpy as np

my_list = [1,2,3]
print(my_list)
np_array = np.array(my_list)
print(np_array)
my_mat = [[1,2,3], [4,5,6], [7,8,9]]
np_mat = np.array(my_mat)
print(np_mat)
print(np.arange(0, 10))     # returns a np array from 0-9
print(np.arange(0, 11, 2))  # returns a np array from 0-10 going by 2's
print(np.zeros((2, 5)))     # returns a np array of zeros
print(np.ones((3, 4)))  # returns a column
print(np.linspace(0, 5, 10))    # one dimensional vector that gives 10 evenly spaced points from 0 to 5
print(np.eye(4))    # Returns an identity matrix of 4x4
print(np.random.random(5))  # returns 5 random array of numbers between 0-1
print(np.random.random((5, 5)))   # returns a 5x5 array of numbers between 0-1
print(np.random.randn(4))   # returns 4 gaussian (-1 to 1)
print(np.random.randn(4, 4))  # returns 4x4 gaussian (-1 to 1)
print(np.random.randint(1, 100, (4, 4)))
arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)
print(arr)
print(ranarr)
arr = arr.reshape(5, 5)
print(arr)
print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())
print(arr.shape)
print(arr.dtype)
