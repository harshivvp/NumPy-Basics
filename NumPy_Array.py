import numpy as np

my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)

my_list2 = [11,22,33,44]

my_lists = [my_list1,my_list2]

print(my_lists , "\n")

my_array2 = np.array(my_lists)

print(my_array2, "\n")

print(my_array2.shape, "\n")

print(my_array2.dtype, "\n")

my_zeros_array = np.zeros(3)

print(my_zeros_array,", ", my_zeros_array.dtype, np.empty(5), "\n")

my_ones_array = np.ones([5,5])

print(my_ones_array, ", ", my_ones_array.dtype, "\n")

print(np.eye(5), '\n') #Identity Matrix, with diagonal number 1 and other numbers 0.

print("Arange : \n" ,np.arange(5))
print(np.arange(5,50), "\n For skipping 2 values in middle :")
print(np.arange(5,50,2), "\n")