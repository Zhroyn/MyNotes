[toc]


## OS模块


#### `os.name`
该属性宽泛地指明了当前 Python 运行所在的环境
- `posix` 是 Portable Operating System Interface of UNIX（可移植操作系统接口）的缩写。Linux 和 Mac OS 均会返回该值
- `nt` 全称应为“Microsoft Windows NT”，大体可以等同于 Windows 操作系统，因此 Windows 环境下会返回该值
- `java` 是 Java 虚拟机环境下的返回值。


#### `os.environ`
该属性可以返回环境相关的信息，主要是各类环境变量

#### `os.walk()`
必须传入一个路径作为top参数，返回一个以top为根节点的目录树的迭代器，对树中的每个目录生成一个由(dirpath, dirnames, filenames)三项组成的三元组
```python
>>> for i in os.walk('D:/Code'):
...     print(i)
...
('D:/Code', ['C', 'Python'], [])
('D:/Code\\C', ['.vscode', 'Algorithm', 'Data Structure', 'test'], ['test1.exe'])
('D:/Code\\C\\.vscode', [], ['c_cpp_properties.json', 'launch.json', 'tasks.json'])
('D:/Code\\C\\Algorithm', ['Sort'], ['BinarySearch.c', 'BinarySearch.exe', 'Floyd.c', 'Floyd.exe', 'Polynomial.c', 'Polynomial.exe'])
('D:/Code\\C\\Algorithm\\Sort', [], ['InsertionSort.c', 'MergeSort.c', 'MergeSort.exe'])
('D:/Code\\C\\Data Structure', ['Graph', 'Linear', 'Tree'], [])
('D:/Code\\C\\Data Structure\\Graph', [], ['LGraph.c', 'LGraph.exe', 'MGraph.c'])
('D:/Code\\C\\Data Structure\\Linear', [], ['Queue.c', 'Queue.exe', 'Queue_int.c', 'Stack.c', 'Stack.exe'])
('D:/Code\\C\\Data Structure\\Tree', [], ['AVLTree.c', 'AVLTree.exe', 'BST_nonrecursive.c', 'BST_nonrecursive.exe', 'BST_recursive.c', 'BST_recursive.exe', 'MaxHeap.c', 'MaxHeap.exe', 'MinHeap.c', 'MinHeap.exe'])
('D:/Code\\C\\test', [], ['temp.c', 'temp.exe', 'test1.c', 'test1.exe', 'test2.c', 'test2.exe', 'test3.c', 'test3.exe'])
('D:/Code\\Python', ['__pycache__'], ['PDF.py', 'PyMuPDF_case.py', 'pynput_keyboard.py', 'pynput_mouse.py', 'temp.py', 'test1.py', 'test2.py'])
('D:/Code\\Python\\__pycache__', [], ['pynput.cpython-310.pyc'])
```

#### `os.listdir()`
