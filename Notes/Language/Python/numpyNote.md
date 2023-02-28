<!-- TOC -->

- [Data Type](#data-type)
- [Array](#array)
  - [Attributes](#attributes)
  - [Create Array](#create-array)
  - [Convert Array](#convert-array)
  - [Index and slice](#index-and-slice)
  - [Search and count](#search-and-count)
  - [Sort](#sort)
  - [Concatenate](#concatenate)
  - [Stack](#stack)
  - [Split](#split)
  - [Reshape](#reshape)
  - [Expand dimension](#expand-dimension)
  - [Transpose](#transpose)
  - [Basic operations](#basic-operations)
- [Random](#random)
  - [Generate random number](#generate-random-number)

<!-- /TOC -->






## Data Type
- `b1` is `bool`
- `b` is `int8`, `i` is `int32`
- `i1, i2, i4, i8` is `int8, int16, int32, int64`
- `u1, u2, u4, u8` is `uint8, uint16, uint32, uint64`
- `f, f2, f4, f8` is `float32, float16, float32, float64`
- `c8, c16` is `complex64, complex128`
- `m, m8` is `timedelta64`
- `M, M8` is `datetime64`
- `O, O8` is `object`
- `c` is `|S1`
- `S, S1, S2, ...` is `|S1, |S1, |S2, ...`
- `a, a1, a2, ...` is `|S1, |S1, |S2, ...`
- `U, U1, U2, ...` is `<U1, <U1, <U2, ...`
<br>

- `np.bool_` is `bool`
- `np.int_, np.intc` is `int32`, `np.intp` is `int64`
- `np.int8, np.int16, np.int32, np.int64` is corresponding integer
- `np.uint8, np.uint16, np.uint32, np.uint64` is corresponding integer
- `np.float_` is `float64`
- `np.float16, np.float32, np.float64` is corresponding float number
- `np.complex_` is `complex128`
- `np.complex64, np.complex128` is corresponding complex number




## Array
### Attributes
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

### Create Array
- `np.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)`
  - `object` : An array, any object exposing the array interface, an object whose `__array__` method returns an array, or any (nested) sequence. If object is a scalar, a 0-dimensional array containing object is returned.
  - `dtype` : If not given, then the type will be determined as the minimum type required to hold the objects.
  - `copy` : If true (default), then the object is copied.  Otherwise, a copy will only be made if `__array__` returns a copy, if obj is a nested sequence, or if a copy is needed to satisfy any of the other requirements (`dtype`, `order`, etc.).
  - `order` : `{'K', 'A', 'C', 'F'}`, optional. If object is not an array, the newly created array will be in C order.
  - `subok` : If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class `array`.
    - `np.array(m, copy=False, subok=True)` will not return a copy.
  - `ndmin` : Specifies the minimum number of dimensions that the resulting array should have. Ones will be pre-pended to the shape as needed to meet this requirement.
<br>

- `np.empty(shape, dtype=float, order='C', *, like=None)`
  - `shape` : int or tuple of int, `np.empty(3)` is equivalent to `np.empty([3])`
- `np.zeros(shape, dtype=float, order='C', *, like=None)`
- `np.ones(shape, dtype=None, order='C', *, like=None)`
  - `dtype` : Default is `numpy.float64`.
- `np.full(shape, fill_value, dtype=None, order='C', *, like=None)`
  - `dtype` : The default, None, means `np.array(fill_value).dtype`.
<br>

- `np.arange([start,] stop[, step,], dtype=None, *, like=None)`
  - `start` : integer or real. The interval includes this value.  The default start value is 0.
  - `stop` : integer or real. The interval does not include this value, except in some cases where `step` is not an integer and floating point round-off affects the length of `out`.
  - `step` : integer or real. The default step size is 1.  If `step` is specified as a position argument, `start` must also be given.
  - `dtype` : If is not given, infer the data type from the other input arguments.
- `np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)`
  - `num` : Number of samples to generate. Default is 50. Must be non-negative.
  - `endpoint` : If True, `stop` is the last sample. Otherwise, it is not included.
  - `retstep` : If True, return (`samples`, `step`), where `step` is the spacing between samples.
  - `dtype` : If is not given, the data type is inferred from `start` and `stop`. The inferred dtype will never be an integer.

### Convert Array
- `np.asarray(a, dtype=None, order=None, *, like=None)`
  - `a` : Input data, in any form that can be converted to an array.  This includes lists, lists of tuples, tuples, tuples of tuples, tuples of lists and ndarrays.
  - `dtype` : By default, the data-type is inferred from the input data.
  - `order` : Memory layout.  'A' and 'K' depend on the order of input array a.
  - Like `np.array(a, copy=False)`, existing arrays are not copied. If `dtype` is set, array is copied only if dtype does not match
- `np.asanyarray(a, dtype=None, order=None, *, like=None)`
  - Like `np.array(a, copy=False, subok=True)`, convert the input to an ndarray, but pass ndarray subclasses through.
- `np.asfarray(a, dtype=<class 'numpy.float64'>)`



### Index and slice
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
### Search and count
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

### Sort
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

### Concatenate
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
### Stack
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
### Split
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
### Reshape
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
```py
# Return a copy of the array collapsed into one dimension.
ndarray.flatten(order='C')

# Return a flattened array.
ndarray.ravel()
# Return a contiguous flattened array.
numpy.ravel(a, order='C')

### When using `flatten`, changes to new array won’t change the parent array.
### When using `ravel`, changes to new array will affect the parent array.
>>> a = np.arange(6).reshape(2, 3)
>>> b = a.flatten()
>>> b[0] = 9
>>> a
array([[0, 1, 2],
       [3, 4, 5]])
>>> b = a.ravel() or np.ravel(a)
>>> b[0] = 9
>>> a
array([[9, 1, 2],
       [3, 4, 5]])
```
### Expand dimension
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
### Transpose
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
```py
# Reverse the order of elements in an array along the given axis.
flip(m, axis=None)
m : array_like
       Input array.
axis : None or int or tuple of ints, optional
       Axis or axes along which to flip over. The default,
       axis=None, will flip over all of the axes of the input array.
       If axis is negative it counts from the last to the first axis.

       If axis is a tuple of ints, flipping is performed on all of the axes
       specified in the tuple.

>>> A = np.arange(8).reshape((2,2,2))
>>> np.flip(A)
array([[[7, 6],
       [5, 4]],
       [[3, 2],
       [1, 0]]])
>>> np.flip(A, (0, 2))
array([[[5, 4],
       [7, 6]],
       [[1, 0],
       [3, 2]]])
```

### Basic operations
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
### Generate random number
```py
# Return a sample (or samples) from the "standard normal" distribution.
np.random.randn(d0, d1, ..., dn)

If positive int_like arguments are provided, an arra of shape ``(d0, d1,
..., dn)``, is returned
If no argument is provided, a single float randomly sampled from the 
distribution is returned
```
```py
# Construct a new Generator with the default BitGenerator (PCG64).
numpy.random.default_rng(...)

>>> rng = np.random.default_rng()
>>> type(rng)
<class 'numpy.random._generator.Generator'>


# Draw samples from a standard Normal distribution (mean=0, stdev=1).
rng.standard_normal(size=None, dtype=np.float64, out=None)
size : int or tuple of ints, optional
       Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
       ``m * n * k`` samples are drawn.  Default is None, in which case a
       single value is returned.
dtype : dtype, optional
       Desired dtype of the result,only `float64` and `float32` are supported
out : ndarray, optional
       Alternative output array in which to place the result.

# Return random floats in the half-open interval [0.0, 1.0).
rng.random(size=None, dtype=np.float64, out=None)
size : int or tuple of ints, optional
       Output shape. Default is None,in which case a single value is returned
dtype : dtype, optional
       Desired dtype of the result,only `float64` and `float32` are supported

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




