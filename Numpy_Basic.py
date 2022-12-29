import numpy as np
'''
#list working

list_a = [1,2,3,4]
list_b = [5,6,7,8]
print(list_a * list_b)'''

'''
import numpy as np
numpy_a = np.array([1,2,3,4])
numpy_b = np.array([5,6,7,8])
print(numpy_a * numpy_b)'''


#basic properties
'''
numpyBasic_array = np.array([1,2,3,4])

print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)

print(numpyBasic_array.size)'''


#
'''
numpyBasic_array = np.array([1,2,3,4,10.9,9.5])

print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)

print(numpyBasic_array.size)'''


#
'''
numpyBasic_array = np.array([1,2,3,4,10.9,9.5,"l"])

print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)

print(numpyBasic_array.size)'''


#2d arrays
# array_1D = np.array(([[[1,2,3],[3,4,5],[[1,2,3],[3,4,5]] ]))
'''array_2D = np.array([[1,2,3],[3,4,5],[6,7,8]])

print(array_2D)
print("Dimensions: {}".format(array_2D.ndim))
print("Shape: {}".format(array_2D.shape))
print("Array Dtype: {}".format(array_2D.dtype))

#3d arrays

array_3d = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(array_3d)

print(array_3d[:,0,:])
array_3d[:,0,:] = [[10,10],[20,20]]
print(array_3d)

four_d = np.zeros((3,3,3,2))
print(four_d)


print(np.full((3,3),[1,2,5]))

print(np.full((2,2),[2,5]))


#repeating
array_r = [[1,2,3],[4,5,6]]
array_repeat = np.repeat(array_r,2,axis=0)
print(array_repeat)

array_r = [[1,2,3],[4,5,6]]
array_repeat = np.repeat(array_r,2,axis=1)
print(array_repeat)

array_zeros = np.zeros((3,3))
array_zeros[1,1] = 7
print(array_zeros)

updated_array = np.zeros((5,5))
updated_array[1:-1,1:-1] = array_zeros

print(updated_array)

#copying arrays

array_x = np.array([1,2,3,4])
array_y = array_x
array_y[0] = 7
print(array_x)
print(array_y)
'''

#math operations
'''
array_math = np.array([1,2,3])
print("Declared array: {}".format(array_math))
print("Add 10 to array: {}".format(array_math + 10))
print("Sub to from array: {}".format(array_math -10))
print("raise to power array: {}".format(array_math **2))
print("mul array by 5: {}".format(array_math *5))
print("div array by 2: {}".format(array_math /2))'''


#
'''
array_stats = [[1,2,3],[4,5,-6],[7,8,0]]

print(np.min(array_stats))
print(np.min(array_stats, axis = 0))
print(np.min(array_stats, axis = 1))

print(np.max(array_stats))
print(np.max(array_stats, axis = 1))'''


#reshape
#arrange - array range
'''one_d = np.arange(6)
print(one_d)


two_d = np.arange(6).reshape(2,3)
print(two_d)

a=np.array((1,2,3))
b=np.array((7,8,6))
np.hstack((a,b))

#numpy as a list
array_l=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(array_l[[1,3,5,7,4]])

############################################333

data_from_text_file = np.genfromtxt('Numpy.txt',delimiter=',')
print(data_from_text_file)

data_from_text = data_from_text_file.astype('int32')
print(data_from_text)
print(data_from_text > 10)
#advance indexing

print(data_from_text[data_from_text > 0])'''

#
def numpy_function(x,y,z):
    return 10*x+y+z
b=np.fromfunction(numpy_function,(2,2,3),dtype=int)
print(b)




