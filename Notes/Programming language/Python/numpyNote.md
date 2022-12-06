[toc]




## Array
#### Creating ndarray
```py
numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
            like=None)
numpy.asarray(a, dtype=None, order=None, *, like=None)
object : array_like
       An array, any object exposing the array interface, an object whose
       __array__ method returns an array, or any (nested) sequence.
       If object is a scalar, a 0-dimensional array containing object is
       returned.
a : array_like
       Input data, in any form that can be converted to an array.  This
       includes lists, lists of tuples, tuples, tuples of tuples, tuples
       of lists and ndarrays.

>>> a = np.array([1, 2, 3])
>>> a = np.array([1, 2, 3], np.int32)
>>> a = np.array([1, 2, 3], 'i4')
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.array([1, 2, 3], ndmin=2)
array([[1, 2, 3]])
>>> np.array(5)
array(5)
>>> np.array(5).reshape(1)
array([5])
```
```py
# Return a new array of given shape and type, filled with ones
numpy.ones(shape, dtype=None, order='C', *, like=None)
# Return a new array of given shape and type, filled with zeros
numpy.zeros(shape, dtype=float, order='C', *, like=None)
# Return a new array of given shape and type, without initializing entries
numpy.empty(shape, dtype=float, order='C', *, like=None)
# Return evenly spaced values within a given interval
numpy.arange([start,] stop[, step,], dtype=None, *, like=None)
# Return evenly spaced numbers over a specified interval
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

>>> np.ones(2, np.int64)
array([1, 1])    # shape: int or tuple of int
>>> np.zeros((2, 1), dtype=float, order='C')
array([[0.],
       [0.]])
>>> np.arange(4)
array([0, 1, 2, 3])
>>> np.arange(5,7,0.2)
array([5. , 5.2, 5.4, 5.6, 5.8, 6. , 6.2, 6.4, 6.6, 6.8])
>>> np.linspace(0, 10, num=5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])

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
# Support multi-dimension index
>>> a[1][1] or a[1, 1]
5
# Support index list or index array
>>> a[ [0, 0, 1, 1], [0, 0, 2, 1] ]
array([1, 1, 6, 5])
# Return a view instead of a copy
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
#### Search and count
```py
# Return the indices of the elements that are non-zero
numpy.nonzero(a)

>>> a = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
>>> a
array([[3, 0, 0],
       [0, 4, 0],
       [5, 6, 0]])
>>> np.nonzero(a)
(array([0, 1, 2, 2]), array([0, 1, 0, 1]))
>>> a[np.nonzero(a)]
array([3, 4, 5, 6])
>>> np.transpose(np.nonzero(a))
array([[0, 0],
       [1, 1],
       [2, 0],
       [2, 1]])
```

#### Sort
```py
# Sort an array in-place
ndarray.sort(axis=-1, kind=None, order=None)
# Return a sorted copy of an array
numpy.sort(a, axis=-1, kind=None, order=None)

axis : int or None, optional
       Axis along which to sort. If None, the array is flattened before
       sorting. The default is -1, which sorts along the last axis.
kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
       Sorting algorithm. The default is 'quicksort'.
order : str or list of str, optional
       When 'a' is an array with fields defined, this argument 
       specifies which fields to compare first, second, etc.


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
axis : int, optional
       The axis along which the arrays will be joined.  If axis is None,
       arrays are flattened before use.  Default is 0.
out : ndarray, optional
       If provided, the destination to place the result. The shape must be
       correct, matching that of what concatenate would have returned if no
       out argument were specified.
dtype : str or dtype
       If provided, the destination array will have this dtype. Cannot be
       provided together with 'out'.

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
#### Stack
```py
# Stack arrays in sequence vertically (row wise).
numpy.vstack(tup)
This is equivalent to concatenation along the first axis after 1-D arrays
of shape `(N,)` have been reshaped to `(1,N)`.
tup : sequence of ndarrays
       The arrays must have the same shape along all but the first axis.
       1-D arrays must have the same length.

# Stack arrays in sequence horizontally (column wise).
numpy.hstack(tup)
This is equivalent to concatenation along the second axis, except for 1-D
arrays where it concatenates along the first axis.
tup : sequence of ndarrays
       The arrays must have the same shape along all but the second axis,
       except 1-D arrays which can be any length.

# Join a sequence of arrays along a new axis.
numpy.stack(arrays, axis=0, out=None)
arrays : sequence of array_like
       Each array must have the same shape.
axis : int, optional
       The axis in the result array along which the input arrays are stacked.
out : ndarray, optional
       The destination to place the result. The shape must be correct.


>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>> np.vstack((a,b))
array([[1, 2, 3],
       [4, 5, 6]])
>>> np.hstack((a,b))
array([1, 2, 3, 4, 5, 6])
>>> np.stack((a, b))
array([[1, 2, 3],
       [4, 5, 6]])
>>> np.stack((a, b), axis=-1)
array([[1, 4],
       [2, 5],
       [3, 6]])
```
#### Split
```py
# Split an array into multiple sub-arrays vertically (row-wise).
numpy.vsplit(ary, indices_or_sections)
'vsplit' is equivalent to 'split' with 'axis=0' (default), the array is
 always split along the first axis regardless of the array dimension.

# Split an array into multiple sub-arrays horizontally (column-wise).
numpy.hsplit(ary, indices_or_sections)
'hsplit' is equivalent to 'split' with 'axis=1', the array is always split
 along the second axis except for 1-D arrays, where it is split at 'axis=0'.

# Split an array into multiple sub-arrays as views into `ary`.
numpy.split(ary, indices_or_sections, axis=0)
indices_or_sections : int or 1-D array
       If `indices_or_sections` is an integer, N, the array will be divided
       into N equal arrays along `axis`.  If such a split is not possible,
       an error is raised.
       If `indices_or_sections` is a 1-D array of sorted integers, the entries
       indicate where along `axis` the array is split. If an index exceeds 
       the dimension of `axis`, an empty sub-array is returned correspondingly.


>>> x = np.arange(9.0)
>>> np.split(x, 3)
[array([0.,  1.,  2.]), array([3.,  4.,  5.]), array([6.,  7.,  8.])]

>>> np.split(x, [3, 5, 6, 10])
[array([0.,  1.,  2.]),
array([3.,  4.]),
array([5.]),
array([6.,  8.]),
array([], dtype=float64)]

>>> np.split(x.reshape(3, 3), [1, 3])
[array([[0., 1., 2.]]),
array([[3., 4., 5.],
       [6., 7., 8.]]),
array([], shape=(0, 3), dtype=float64)]
```
#### Reshape
```py
# Returns an array containing the same data with a new shape.
ndarray.reshape(shape, order='C')
numpy.reshape(a, newshape, order='C')
### Notes: "ndarray.reshape" allows the elements of
### the shape parameter to be passed in as separate arguments

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
>>> np.resize(a,(2,4))
array([[0, 1, 2, 3],
       [0, 1, 2, 3]])
```
#### Expand dimension
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
numpy.expand_dims(a, axis)
axis : int or tuple of ints

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
#### Transpose
```py
# Reverse or permute the axes of an array; returns the modified array
numpy.transpose(a, axes=None)
a : array_like
       Input array.
axes : tuple or list of ints, optional
       If not specified, defaults to ``range(a.ndim)[::-1]``, which
       reverses the order of the axes.

>>> np.transpose(np.arange(4).reshape(2, 2))
array([[0, 2],
       [1, 3]])
>>> a = np.ones((2, 3, 4, 5))
>>> np.transpose(a).shape
(5, 4, 3, 2)
>>> a = np.ones((1, 2, 3))
>>> np.transpose(a, (1, 0, 2)).shape
(2, 1, 3)
```

#### Basic operations
```py
>>> data = np.array([1, 2])
>>> ones = np.ones(2, dtype=int)

### Operation between a array and a scalar
>>> data + 1
array([2, 3])
>>> data - 1
array([0, 1])
>>> data * 2
array([2, 4])
>>> data / 2
array([0.5, 1. ])

### Operation between arrays with the same shape
>>> data + ones
array([2, 3])
>>> data - ones
array([0, 1])
>>> data * data
array([1, 4])
>>> data / data
array([1., 1.])

### Operation between arrays with different shapes
>>> a = np.arange(1, 25, dtype='i4').reshape(2, 3, 4)
>>> a + np.ones(4, 'i4').reshape(4)
array([[[ 2,  4,  6,  8],
        [ 6,  8, 10, 12],
        [10, 12, 14, 16]],

       [[14, 16, 18, 20],
        [18, 20, 22, 24],
        [22, 24, 26, 28]]])
>>> a + np.ones(12, 'i4').reshape(3, 4)
array([[[ 2,  3,  4,  5],
        [ 6,  7,  8,  9],
        [10, 11, 12, 13]],

       [[14, 15, 16, 17],
        [18, 19, 20, 21],
        [22, 23, 24, 25]]])


### More operations
>>> a.sum()
300
>>> a.sum(0)
array([[14, 16, 18, 20],
       [22, 24, 26, 28],
       [30, 32, 34, 36]])
>>> a.sum(1)
array([[15, 18, 21, 24],
       [51, 54, 57, 60]])

>>> a.min()
1
>>> a.min(2)
array([[ 1,  5,  9],
       [13, 17, 21]])
>>> a.max(2)
array([[ 4,  8, 12],
       [16, 20, 24]])
```





## Random
```py
# Construct a new Generator with the default BitGenerator (PCG64).
numpy.random.default_rng(...)

>>> rng = np.random.default_rng()
>>> type(rng)
<class 'numpy.random._generator.Generator'>
```
```py
# Return random floats in the half-open interval [0.0, 1.0).
rng.random(size=None, dtype=np.float64, out=None)
size : int or tuple of ints, optional
       Output shape. Default is None, in which case a single value is returned.
dtype : dtype, optional
       Desired dtype of the result, only `float64` and `float32` are supported.

# Return random integers
rng.integers(low, high=None, size=None, dtype=np.int64, endpoint=False)
low : int or array-like of ints
       Lowest (signed) integers to be drawn (unless ``high=None``, in which 
       case this parameter is 0 and this value is used for `high`).
high : int or array-like of ints, optional
       If provided, one above the largest (signed) integer to be drawn
       from the distribution.
       If array-like, must contain integer values
size : int or tuple of ints, optional
       Output shape.
dtype : dtype, optional
       Desired dtype of the result. Byteorder must be native.
       The default value is np.int64.
endpoint : bool, optional
       If true, sample from the interval [low, high] instead of the
       default [low, high)


```




