# 4. Profiling and Optimization

Full list of references of Chapter 4 of the [IPython Cookbook][http://ipython-books.github.io), the definitive guide to high-performance scientific computing and data science in Python, by Dr. Cyrille Rossant, Packt Publishing, 400 pages, 2014.

## Profiling

* [Program optimization on Wikipedia](http://en.wikipedia.org/wiki/Program_optimization).
* [Python's `timeit` module](http://docs.python.org/3/library/timeit.html).
* [Python's `profile` module](http://docs.python.org/3/library/profile.html).
* [`easy_profiler` that simplifies the use of Python profiling tools](http://github.com/rossant/easy_profiler).
* [`line_profiler`, a line-by-line profiler, for Python 2 only](http://pythonhosted.org/line_profiler/).
* [How to deal with `@profile` in profiled code](http://stackoverflow.com/questions/18229628/python-profiling-using-line-profiler-clever-way-to-remove-profile-statements).
* [RunSnakeRun, a viewer for profiling results](http://www.vrplumber.com/programming/runsnakerun/).


## Memory profiling

* [`memory_profiler` package](http://pypi.python.org/pypi/memory_profiler).
* [`psutil` package, required by `memory_profiler`](http://pypi.python.org/pypi/psutil).
* [Guppy-PE, a memory profiling package](http://guppy-pe.sourceforge.net).
* [PySizer, a memory profiler for Python](http://pysizer.8325.org).
* [Pympler, another memory profiler](http://code.google.com/p/pympler/).


## Code tracing

* [Python's `trace` module](https://docs.python.org/3/library/trace.html).
* [Online Python Tutor, a great educational interactive tool to visualize the step-by-step execution of Python code](http://pythontutor.com/).
* [Some Python profiling tools](http://blog.ionelmc.ro/2013/06/08/python-profiling-tools/).


## NumPy code optimization

* [Broadcasting rules and examples](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).
* [Array interface in NumPy](http://docs.scipy.org/doc/numpy/reference/arrays.interface.html).
* [Locality of reference](http://en.wikipedia.org/wiki/Locality_of_reference).
* [Internals of NumPy in the SciPy lectures notes](http://scipy-lectures.github.io/advanced/advanced_numpy/).
* [The complete list of NumPy routines is available on the NumPy Reference Guide](http://docs.scipy.org/doc/numpy/reference/).
* [List of indexing routines](http://docs.scipy.org/doc/numpy/reference/routines.indexing.html).
* [100 NumPy exercices](http://www.loria.fr/~rougier/teaching/numpy.100/index.html).


## Memory mapping

* [Documentation of memmap](http://docs.scipy.org/doc/numpy/reference/generated/numpy.memmap.html).


## Sparse matrices

* [SciPy lecture notes about sparse matrices](http://scipy-lectures.github.io/advanced/scipy_sparse/index.html).
* [Reference documentation on sparse matrices](http://docs.scipy.org/doc/scipy/reference/sparse.html).


## HDF5

* [PyTables](http://pytables.github.io)
* [h5py](http://www.h5py.org)
* [Partial list of HDF5 users](http://www.hdfgroup.org/users.html)
* [HDF5 chunking](http://www.hdfgroup.org/HDF5/doc/Advanced/Chunking/).
* [PyTables optimization guide, a must-read for PyTables users](http://pytables.github.io/usersguide/optimization.html).
* [In-kernel queries](http://pytables.github.io/usersguide/condition_syntax.html).
* [An alternative to PyTables and HDF5 might come from the Blaze project, still in early development at the time of writing](http://blaze.pydata.org).
* [Difference between PyTables and h5py, from the perspective of h5py](http://github.com/h5py/h5py/wiki/FAQ#whats-the-difference-between-h5py-and-pytables).
* [Difference between PyTables and h5py, from the perspective of PyTables](http://www.pytables.org/moin/FAQ#HowdoesPyTablescomparewiththeh5pyproject.3F).

