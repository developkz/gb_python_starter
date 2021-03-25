import numpy as np
from numpy import sqrt
from math import sqrt as sqrt_int
import user_info
import time
import sys


new_arr = []
print(sys.argv)
print(sys.argv[2])
python_list = list(range(0, int(sys.argv[1]), 2))
numpy_list = np.array(python_list)

# print(sqrt(test_int))
start_list = time.perf_counter()
list_test = (list(map(sqrt_int, python_list)))
finish_list = time.perf_counter()

user_info.our_print.user_print('Name', 37.7, 'KFC', True)

# for el in python_list:
#     new_arr.append(sqrt(el))
# print(new_arr)
# # print(type(numpy_list))
start_numpy = time.perf_counter()
numpy_test = sqrt(numpy_list)
finish_numpy = time.perf_counter()

print(f'List time:{finish_list - start_list},'
      f'Numpy time: {finish_numpy - finish_list}')
