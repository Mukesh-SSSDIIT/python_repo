import numpy as np

zero_d_arr = np.array(10)
print(zero_d_arr)
print(zero_d_arr.ndim)
print(zero_d_arr)

one_d_arr = np.array([10,20,30,40])
print(one_d_arr)
print(one_d_arr.ndim)
print(one_d_arr[0])

two_d_arr = np.array([[10,20,30],[40,50,60]])
print(two_d_arr)
print(two_d_arr.ndim)
print(two_d_arr[0,0])

three_d_arr = np.array([[[10,20,30],[40,50,60]]])
print(three_d_arr)
print(three_d_arr.ndim)
print(three_d_arr[0,0,0])

four_d_arr = np.array([10,20],ndmin=4)
print(four_d_arr)
print(four_d_arr[0,0,0,0])