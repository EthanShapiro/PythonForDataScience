import numpy as np

# 1 Dimensional array
arr = np.arange(0, 10)
print(arr)
print(arr[8])
print(arr[1:5])
print(arr[::2])
arr[0:5] = 100
print(arr)
arr = np.arange(0, 10)
print(arr)
slice_of_arr = arr[:6]
print(slice_of_arr)
print(slice_of_arr[:])
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr)
arr_copy = arr.copy()
print(arr)
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)

# Matrix
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d[0][0])
print(arr_2d[1][0])
print(arr_2d[0, 0])
print(arr_2d[1, 0])
print(arr_2d[:, :2])
print(arr_2d[:2])
arr = np.arange(1, 11)
print(arr)
bool_arr = arr > 5
print(bool_arr)
print(arr[bool_arr])
print(arr[arr > 5])
print(arr[arr < 3])

arr_2d = np.arange(50).reshape(5, 10)
print(arr_2d)
print(arr_2d[1:3, 3:5])
