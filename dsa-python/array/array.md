An array is a data structure that stores elements in contiguous memory locations and allows access using an index.

arr = [10,20,30,40]

Arrays are foundation of :
    - Searching
    - Sorting
    - Strings
    - Matrices
    - Hashing (Indirectly) (Hash tables internally use arrays for buckets)

Arrays allow efficient indexed access but can be inefficient for insertion and deletion due to shifting.

In low-level languages (C/C++), arrays are fixed-size and homogeneous.
In high-level languages like Python, lists are dynamic arrays and can be heterogeneous.

In Python, lists are used instead of traditional arrays because they are dynamic and flexible. Python also provides array-like structures through the array module and libraries like NumPy for numerical computing.


Difference between Array and list
                 Array                                     List
Data Type        Homogenous.                               Heterogenous
Flexibility      Fixed (C) / Dynamic (NumPy internally)    Dynamic
Memory           More memory efficient                     More Overhead
Performance      Faster for numerical computation          Slower for large numeric data
Usage in Python  Use array or numpy                        Built in



Lists are not always slower.
They are slower mainly for: large numeric computations , scientific workloads.


### IMP to remember
Arrays → fast access, slow modification
Fixed size → language dependent
Python lists → dynamic arrays, not classic arrays
Homogeneous vs heterogeneous → important distinction
NumPy arrays ≠ Python lists