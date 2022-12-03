[toc]




## Array
#### Creating ndarray
```py
numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
            like=None)
numpy.asarray(a, dtype=None, order=None, *, like=None)

>>> a = np.array([1, 2, 3])
>>> a = np.array([1, 2, 3], np.int32)
>>> a = np.array([1, 2, 3], 'i4')
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.array([1, 2, 3], ndmin=2)
array([[1, 2, 3]])
```
```py
>>> np.zeros(2)     #create an array filled with 0’s
array([0., 0.])
>>> np.ones(2)      #create an array filled with 1’s
array([1., 1.])
>> np.empty(2)      #create an empty array which may vary
array([3.14, 42.])
>>> np.arange(4)    #create an array with a range of elements
array([0, 1, 2, 3])
>>> np.linspace(0, 10, num=5) #create an array with values distributing evenly
array([ 0. ,  2.5,  5. ,  7.5, 10. ])

# Specifying data type, which is 'np.float64' by default
>>> np.ones(2, np.int64)
array([1, 1])
# Specifying shape, data type, and order
>>> np.zeros((2, 1), dtype=float, order='C')
```
#### Creating dtype
```py
# Any string in numpy.sctypeDict.keys():
dt = np.dtype('uint32')       # 32-bit unsigned integer
dt = np.dtype('float64')      # 64-bit floating-point number

# (flexible_dtype, itemsize)
dt = np.dtype((np.void, 10))  # 10-byte wide data block
dt = np.dtype(('U', 10))      # 10-character unicode string

# (fixed_dtype, shape)
dt = np.dtype((np.int32, (2,2)))          # 2 x 2 integer sub-array
dt = np.dtype(('i4, (2,3)f8, f4', (2,3))) # 2 x 3 structured sub-array

# [(field_name, field_dtype, field_shape), ...]
### If the field_name is '' then a standard field name 'f#' is assigned.
dt = np.dtype([('big', '>i4'), ('little', '<i4')])
dt = np.dtype([('R','u1'), ('G','u1'), ('B','u1'), ('A','u1')])

# {'names': ..., 'formats': ..., 'offsets': ..., 'titles': ..., 'itemsize': ...}
### The names and formats keys are required. The field names must be strings.
dt = np.dtype({'names': ['r','g','b','a'],
               'formats': [np.uint8, np.uint8, np.uint8, np.uint8]})

# {'field1': ..., 'field2': ..., ...}
### This usage is discouraged, because it is ambiguous.
### obj should contain string or (data-type, offset, title) tuples, etc
dt = np.dtype({'col1': ('U10', 0), 'col2': (np.float32, 10),
               'col3': (int, 14)})


>>> dt = np.dtype(('i4', 5))
>>> a = np.array([1,2,3], dt)
>>> a[1]
array([2, 2, 2, 2, 2])

>>> dt = np.dtype([('R','u1'), ('G','u1'), ('B','u1'), ('A','u1')])
>>> a = np.array([1,2,3], dt)
>>> a[1]
(2, 2, 2, 2)

>>> dt = np.dtype(('i4', (3, 2)))
>>> a = np.array([1,2,3], dt)
>>> a[1]
array([[2, 2],
       [2, 2],
       [2, 2]])

>>> dt = np.dtype(('i4, (2,3)f8, f4', (2,3)))
>>> a = np.array([1,2,3], dt)
>>> a[1][1]
array([(2, [[2., 2., 2.], [2., 2., 2.]], 2.),
       (2, [[2., 2., 2.], [2., 2., 2.]], 2.),
       (2, [[2., 2., 2.], [2., 2., 2.]], 2.)],
      dtype=[('f0', '<i4'), ('f1', '<f8', (2, 3)), ('f2', '<f4')])
```


#### Attributes
```py
ndarray.flags    # Information about the memory layout of the array
ndarray.shape    # Tuple of array dimensions
ndarray.strides  # Tuple of bytes to step in each dimension when traversing array
ndarray.ndim     # Number of array dimensions
ndarray.data     # Python buffer object pointing to the start of the array's data
ndarray.size     # Number of elements in the array
ndarray.itemsize # Length of one array element in bytes
```
```py
>>> a.flags
  C_CONTIGUOUS : True
  F_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False

>>> a.shape
(2, 3)
>>> a.strides
(12, 4)
>>> a.ndim
2
>>> a.data
<memory at 0x000002E067F039F0>
>>> a.size
6
>>> a.itemsize
4
>>> a.dtype
dtype('int32')
```
#### Index and slice
```py
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> a[1][1] or a[1, 1]
5
>>> b = a[0]
>>> b[0] = 9    # Different ndarrays can share the same data
>>> a
array([[1, 9, 3],
       [4, 5, 6]])


>>> a[:, 1]
array([2, 5])

>>> (a > 5) | (a == 5)
array([[False, False, False],
       [False,  True,  True]])
>>> a[(a > 5) | (a == 5)]
array([5, 6])
>>> a[a % 2 == 0]
array([2, 4, 6])
>> a[(a > 2) & (a <= 5)]
array([3, 4, 5])

>>> np.nonzero(a < 5)
(array([0, 0, 0, 1], dtype=int64), array([0, 1, 2, 0], dtype=int64))
>>> a[np.nonzero(a < 5)]
array([1, 2, 3, 4])
```

#### Sort, search and count
```py
# Sort an array in-place
ndarray.sort(axis=- 1, kind=None, order=None)
# Return a sorted copy of an array
numpy.sort(a, axis=- 1, kind=None, order=None)[source]

axis  # int or None, optional. Axis along which to sort
# If None, the array is flattened before sorting.
# The default is -1, which sorts along the last axis.
kind  # Optional sorting algorithm, the default is ‘quicksort’.
# {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}
order # str or list of str, optional
# specifies which fields to compare first, second, etc.

>>> a = np.array([[1,4],[3,1]])
>>> np.sort(a)            # sort along the last axis
array([[1, 4],
       [1, 3]])
>>> np.sort(a, axis=None) # sort the flattened array
array([1, 1, 3, 4])
>>> np.sort(a, axis=0)    # sort along the first axis
array([[1, 1],
       [3, 4]])

>>> dtype = [('name', 'S10'), ('height', float), ('age', int)]
>>> values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
>>> a = np.array(values, dtype=dtype) # create a structured array
# Sort by height:
>>> np.sort(a, order='height')
# Sort by age, then height if ages are equal:
>>> np.sort(a, order=['age', 'height'])
```

#### Concatenate
```py
# Join a sequence of arrays along an existing axis
numpy.concatenate((a1, a2, ...), axis=0, out=None, dtype=None, ...)

out   # ndarray, optional. The destination to place the result.
dtype # str or dtype. If provided, the destination array will have this dtype.
# Cannot be provided together with out.

>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6]])
>>> np.concatenate((a, b), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
>>> np.concatenate((a, b), axis=None)
array([1, 2, 3, 4, 5, 6])
```

#### Reshape and convert dimension
```py
# Returns an array containing the same data with a new shape.
ndarray.reshape(shape, order='C')
numpy.reshape(a, newshape, order='C')

>>> a = np.arange(6)
>>> a.reshape(3, 2)
array([[0, 1],
       [2, 3],
       [4, 5]])
>>> np.reshape(a, newshape=(1, 6))
array([[0, 1, 2, 3, 4, 5]])
```
```py
# Return a flattened array.
ndarray.ravel()
# Return a contiguous flattened array.
numpy.ravel(a, order='C')
# Change shape and size of array in-place.
ndarray.resize(new_shape, refcheck=True)
# Return a new array with the specified shape.
numpy.resize(a, new_shape)

>>> a = np.array([[0,1],[2,3]])
>>> a.ravel()
array([0, 1, 2, 3])
>>> np.resize(a,(2,3))
array([[0, 1, 2],
       [3, 0, 1]])
>>> np.resize(a,(1,4))
array([[0, 1, 2, 3]])
>>> np.resize(a,(2,4))
array([[0, 1, 2, 3],
       [0, 1, 2, 3]])
```
```py
# Insert a new axis that will appear at the 'np.newaxis' position
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> a.shape
(6,)
>>> row_vector = a[np.newaxis, :]
>>> row_vector.shape
(1, 6)
>>> col_vector = a[:, np.newaxis]
>>> col_vector.shape
(6, 1)

# Insert a new axis that will appear at the 'axis' position
expand_dims(a, axis)
>>> np.expand_dims(a, axis=1).shape
(6, 1)
>>> np.expand_dims(a, axis=0).shape
(1, 6)
>>> a = np.arange(6).reshape((2, 3))
>>> np.expand_dims(a, (0, 1)).shape
(1, 1, 2, 3)
>>> np.expand_dims(a, (1, 0)).shape
(1, 1, 2, 3)
>>> np.expand_dims(a, (0, 2)).shape
(1, 2, 1, 3)
```









