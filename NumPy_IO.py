import numpy as np

arr = np.arange(5)

np.save('NumPy_Array',arr)

arr = np.arange(10)

print(np.load('NumPy_Array.npy'))

arr1 = np.load('NumPy_Array.npy')
arr2 = arr

print()
print(arr1)
print(arr2)

np.savez('ziparray.npz', x = arr1, y = arr2)

archive_array = np.load('ziparray.npz')

print()
print(archive_array)

print(archive_array['x'])
print(archive_array['y'])

arr = np.array([[1,2,3],[4,5,6]])

print()
print(arr)

np.savetxt('mytxtarray.txt',arr,delimiter=',')
print(np.loadtxt('mytxtarray.txt',delimiter=','))