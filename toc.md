# IPython Cookbook: the Table of Contents

* [A one-stop guide for **high-performance scientific computing** and **data science** in Python](http://ipython-books.github.io/).
* More than 100 hands-on, ready-to-use, highly focused recipes with diverse real-world examples and clear, detailed step-by-step explanations.
* All the code is available as IPython notebooks.
    
## Part I: Advanced High-Performance Interactive Computing

Part I (chapters 1-6) covers advanced methods in interactive numerical computing, high-performance computing, and data visualization.

### Chapter 1: A Tour of Interactive Computing with IPython

This chapter contains a brief but intense introduction to data analysis and numerical computing with IPython. It not only covers common packages such as **NumPy**, **pandas**, and **matplotlib**, but also advanced IPython topics such as **interactive widgets** in the notebook, **custom magic commands**, configurable **IPython extensions**, and new language kernels.

* [1.1. Introducing the IPython notebook](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter01_basic/01_notebook.ipynb)
* [1.2. Getting started with exploratory data analysis in IPython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter01_basic/02_pandas.ipynb)
* [1.3. Introducing the multidimensional array in NumPy for fast array computations](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter01_basic/03_numpy.ipynb)
* [1.4. Creating an IPython extension with custom magic commands](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter01_basic/04_magic.ipynb)
* [1.5. Mastering IPython's configuration system](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter01_basic/05_config.ipynb)
* [1.6. Creating a simple kernel for IPython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter01_basic/06_kernel.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter01_intro.md)


### Chapter 2: Best practices in Interactive Computing

This chapter details best practices for writing reproducible, high-quality code: task automation, **version control systems with Git**, workflows with IPython, **unit testing** with nose, **continuous integration**, debugging, and other related topics. The importance of these subjects in computational research and data analysis cannot be overstated.

* 2.1. Choosing between Python 2 and Python 3 (or not)
* 2.2. Efficient interactive computing workflows with IPython
* 2.3. Learning the basics of the distributed version control system Git
* 2.4. A typical workflow with Git branching
* 2.5. Ten tips for conducting reproducible interactive computing experiments
* 2.6. Writing high-quality Python code
* 2.7. Writing unit tests with nose ([Python 2](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter02_best_practices/07_unittests_py2.ipynb) or [Python 3](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter02_best_practices/07_unittests.ipynb))
* 2.8. Debugging your code with IPython
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter02_best_practices.md)


### Chapter 3: Mastering the Notebook

This chapter covers advanced topics related to the IPython notebook, notably the **notebook format**, notebook conversions with **nbconvert**, and **CSS/Javascript customization**. The new **interactive widgets** available in IPython 2.0+ are also extensively covered. These techniques make data analysis in the notebook more interactive than ever.

* [3.1. Teaching programming in the notebook with IPython blocks](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/01_blocks.ipynb)
* [3.2. Converting an IPython notebook to other formats with nbconvert](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/02_nbformat.ipynb)
* [3.3. Adding custom controls in the notebook toolbar](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/03_controls.ipynb)
* [3.4. Customizing the CSS style in the notebook](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/04_css.ipynb)
* [3.5. Using interactive widgets: a piano in the notebook](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/05_basic_widgets.ipynb)
* [3.6. Creating a custom Javascript widget in the notebook: a spreadsheet editor for Pandas](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/06_widgets.ipynb)
* 3.7. Processing webcam images in real-time from the notebook: [Python 2](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/07_webcam_py2.ipynb) and [Python 3](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter03_notebook/07_webcam_py3.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter03_notebook.md)


### Chapter 4: Profiling and Optimization

This chapter covers methods for making your code faster and more efficient: **CPU and memory profiling** in Python, **advanced NumPy optimization techniques** (including large array manipulations), and **memory mapping** of huge arrays with the **HDF5** file format and the **PyTables** library. These techniques are essential for big data analysis.

* [4.1. Evaluating the time taken by a statement in IPython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/01_timeit.ipynb)
* [4.2. Profiling your code easily with cProfile and IPython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/02_profile.ipynb)
* [4.3. Profiling your code line by line with line_profiler](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/03_linebyline.ipynb)
* [4.4. Profiling the memory usage of your code with memory_profiler](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/04_memprof.ipynb)
* [4.5. Understanding the internals of NumPy to avoid unnecessary array copying](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/05_array_copies.ipynb)
* [4.6. Using stride tricks with NumPy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/06_stride_tricks.ipynb)
* [4.7. Implementing an efficient rolling average algorithm with stride tricks](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/07_rolling_average.ipynb)
* [4.8. Making efficient selections in arrays with NumPy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/08_efficient_selections.ipynb)
* [4.9. Processing huge NumPy arrays with memory mapping](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/09_memmap.ipynb)
* [4.10. Manipulating large arrays with HDF5 and PyTables](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/10_hdf5_array.ipynb)
* [4.11. Manipulating large heterogeneous tables with HDF5 and PyTables](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter04_optimization/11_hdf5_table.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter04_optimization.md)


### Chapter 5: High-Performance Computing

This chapter covers advanced techniques for making your code much faster: code acceleration with **Numba** and **Cython**, wrapping of C libraries in Python with **ctypes**, parallel computing with IPython, **OpenMP** and **MPI**, and General-Purpose Computing on Graphics Processing Units (**GPGPU**) with **CUDA** and **OpenCL**. The chapter ends with an introduction to the recent **Julia** language, designed for high-performance numerical computing, and which can be easily used in the IPython notebook.

* [5.1. Accelerating pure Python code with Numba and Just-In-Time compilation](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/01_numba.ipynb)
* [5.2. Accelerating array computations with Numexpr](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/02_numexpr.ipynb)
* [5.3. Wrapping a C library in Python with ctypes](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/03_ctypes.ipynb)
* [5.4. Accelerating Python code with Cython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/04_cython.ipynb)
* 5.5.Optimizing Cython code by writing less Python and more C
    * [Pure Python](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/05_ray_1.ipynb)
    * [Naive Cython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/05_ray_2.ipynb)
    * [Cython with array buffers](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/05_ray_3.ipynb)
    * [Cython with tuples](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/05_ray_4.ipynb)
    * [Cython with structs](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/05_ray_5.ipynb)
* 5.6. Releasing the GIL to take advantage of multi-core processors with Cython and OpenMP: [Windows](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/06_openmp_windows.ipynb) or [Linux](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/06_openmp_linux.ipynb)
* [5.7. Writing massively parallel code for NVIDIA graphics cards (GPUs) with CUDA](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/07_cuda.ipynb)
* [5.8. Writing massively parallel code for heterogeneous platforms with OpenCL](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/08_opencl.ipynb)
* [5.9. Distributing Python code across multiple cores with IPython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/09_ipyparallel.ipynb)
* [5.10. Interacting with asynchronous parallel tasks in IPython](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/10_async.ipynb)
* [5.12. Trying the Julia language in the notebook](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter05_hpc/12_julia.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter05_hpc.md)



### Chapter 6: Advanced Visualization

This chapter introduces a few data visualization libraries that go beyond matplotlib in terms of styling or programming interfaces (**prettyplotlib** and **seaborn**). It also covers interactive visualization in the notebook with **Bokeh**, **mpld3**, and **D3.js**. The chapter ends with an introduction to **Vispy**, a library that leverages the power of Graphics Programming Units (**GPUs**) for high-performance interactive visualization of big data.

* [6.1. Making nicer matplotlib figures with prettyplotlib](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter06_viz/01_prettyplotlib.ipynb)
* [6.2. Creating beautiful statistical plots with seaborn](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter06_viz/02_seaborn.ipynb)
* [6.3. Creating interactive Web visualizations with Bokeh](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter06_viz/03_bokeh.ipynb)
* [6.4. Visualizing a NetworkX graph in the IPython notebook with d3.js](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter06_viz/04_d3.ipynb)
* [6.5. Converting matplotlib figures to d3.js visualizations with mpld3](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter06_viz/05_mpld3.ipynb)
* [6.6. Getting started with Vispy for high-performance interactive data visualizations](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter06_viz/06_vispy.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter06_viz.md)


## Part II: Standard Methods in Data Science and Applied Mathematics

Part II (chapters 7-15) introduces standard methods in data science and mathematical modeling. All of these methods are applied to real-world data.


### Chapter 7: Statistical Data Analysis

This chapter covers methods for getting insight into data. It introduces classic **frequentist and Bayesian methods** for **hypothesis testing**, parametric and nonparametric **estimation**, and model **inference**. The chapter leverages Python libraries such as pandas, SciPy, **statsmodels**, and **PyMC**. The last recipe introduces the statistical language **R**, which can be easily used in the notebook.

* [7.1. Exploring a dataset with Pandas and matplotlib](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/01_pandas.ipynb)
* [7.2. Getting started with statistical hypothesis testing: a simple z-test](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/02_z_test.ipynb)
* [7.3. Getting started with Bayesian methods](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/03_bayesian.ipynb)
* [7.4. Estimating the correlation between two variables with a contingency table and a chi-square test](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/04_correlation.ipynb)
* [7.5. Fitting a probability distribution to data with the maximum likelihood method](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/05_mlfit.ipynb)
* [7.6. Estimating a probability distribution nonparametrically with a Kernel Density Estimation](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/06_kde.ipynb)
* [7.7. Fitting a Bayesian model by sampling from a posterior distribution with a Markov Chain Monte Carlo method](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/07_pymc.ipynb)
* [7.8. Analyzing data with R in the IPython notebook](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter07_stats/08_r.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter07_stats.md)


### Chapter 8: Machine Learning

This chapter covers methods for learning and making predictions from data. Using the **scikit-learn** Python package, this chapter illustrates fundamental data mining and machine learning concepts such as **supervised and unsupervised learning**, **classification**, **regression**, feature selection, feature extraction, overfitting, regularization, cross-validation, and grid search. Algorithms addressed in this chapter include logistic regression, Naive Bayes, K-nearest neighbors, Support Vector Machines, random forests, and others. These methods are applied to various types of datasets: numerical data, images, and text.

* [8.1. Getting started with scikit-learn](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/01_scikit.ipynb)
* [8.2. Predicting who will survive on the Titanic with logistic regression](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/02_titanic.ipynb)
* [8.3. Learning to recognize handwritten digits with a K-nearest neighbors classifier](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/03_digits.ipynb)
* [8.4. Learning from text: Naive Bayes for Natural Language Processing](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/04_text.ipynb)
* [8.5. Using Support Vector Machines for classification tasks](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/05_svm.ipynb)
* [8.6. Using a random forest to select important features for regression](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/06_random_forest.ipynb)
* [8.7. Reducing the dimensionality of a data with a Principal Component Analysis](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/07_pca.ipynb)
* [8.8. Detecting hidden structures in a dataset with clustering](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter08_ml/08_clustering.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter08_ml.md)



### Chapter 9: Numerical Optimization

This chapter is about minimizing or maximizing mathematical functions. This topic is pervasive in data science, notably in statistics, machine learning, and signal processing. This chapter illustrates a few root-finding, minimization, and curve fitting routines with SciPy.

* [9.1. Finding the root of a mathematical function](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter09_numoptim/01_root.ipynb)
* [9.2. Minimizing a mathematical function](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter09_numoptim/02_minimize.ipynb)
* [9.3. Fitting a function to data with nonlinear least squares](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter09_numoptim/03_curvefitting.ipynb)
* [9.4. Finding the equilibrium state of a physical system by minimizing its potential energy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter09_numoptim/04_energy.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter09_numopt.md)


### Chapter 10: Signal Processing

This chapter is about extracting relevant information from complex and noisy data. These steps are sometimes required prior to running statistical and data mining algorithms. This chapter introduces standard signal processing methods like Fourier transforms and digital filters.

* [10.1. Analyzing the frequency components of a signal with a Fast Fourier Transform](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter10_signal/01_fourier.ipynb)
* [10.2. Applying a linear filter to a digital signal](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter10_signal/02_filter.ipynb)
* [10.3. Computing the autocorrelation of a time series](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter10_signal/03_autocorrelation.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter10_signal.md)


### Chapter 11: Image and Audio Processing

This chapter covers signal processing methods for images and sounds. It introduces image filtering, segmentation, computer vision, and face detection with **scikit-image** and **OpenCV**. It also presents methods for audio processing and synthesis.

* [11.1. Manipulating the exposure of an image](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/01_exposure.ipynb)
* [11.2. Applying filters on an image](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/02_filters.ipynb)
* [11.3. Segmenting an image](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/03_segmentation.ipynb)
* [11.4. Finding points of interest in an image](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/04_interest.ipynb)
* [11.5. Detecting faces in an image with OpenCV](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/05_faces.ipynb)
* 11.6. Applying digital filters to speech sounds: [Python 2](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/06_speech_py2.ipynb) or [Python 3](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/06_speech.ipynb)
* [11.7. Creating a sound synthesizer in the notebook](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter11_image/07_synth.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter11_image.md)


### Chapter 12: Deterministic Dynamical Systems

This chapter describes dynamical processes underlying particular types of data. It illustrates simulation techniques for discrete-time dynamical systems, as well as for both Ordinary Differential Equations (**ODEs**) and Partial Differential Equations (**PDEs**).

* [12.1. Plotting the bifurcation diagram of a chaotic dynamical system](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter12_deterministic/01_bifurcation.ipynb)
* [12.2. Simulating an elementary cellular automaton](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter12_deterministic/02_cellular.ipynb)
* [12.3. Simulating an Ordinary Differential Equation with SciPy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter12_deterministic/03_ode.ipynb)
* [12.4. Simulating a Partial Differential Equation: reaction-diffusion systems and Turing patterns](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter12_deterministic/04_turing.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter12_deterministic.md)


### Chapter 13: Stochastic Dynamical Systems

This chapter describes dynamical random processes underlying particular types of data. It illustrates simulation techniques for discrete-time Markov chains, point processes, and stochastic differential equations.

* [13.1. Simulating a discrete-time Markov chain](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter13_stochastic/01_markov.ipynb)
* [13.2. Simulating a Poisson process](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter13_stochastic/02_poisson.ipynb)
* [13.3. Simulating a Brownian motion](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter13_stochastic/03_brownian.ipynb)
* [13.4. Simulating a stochastic differential equation](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter13_stochastic/04_sde.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter13_stochastic.md)


### Chapter 14: Graphs, Geometry, and Geographic Information Systems

This chapter covers analysis and visualization methods for graphs, social networks, road networks, maps, and geographic data.

* [14.1. Manipulating and visualizing graphs with NetworkX](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/01_networkx.ipynb)
* [14.2. Analyzing a social network with NetworkX](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/02_social.ipynb)
* [14.3. Resolving dependencies in a Directed Acyclic Graph with a topological sort](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/03_dag.ipynb)
* [14.4. Computing connected components in an image](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/04_connected.ipynb)
* [14.5. Computing the Voronoi diagram of a set of points](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/05_voronoi.ipynb)
* [14.6. Manipulating geospatial data with Shapely and basemap](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/06_gis.ipynb)
* [14.7. Creating a route planner for road network](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter14_graphgeo/07_gps.ipynb)
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter14_graphs.md)



### Chapter 15: Symbolic and Numerical Mathematics

This chapter introduces **SymPy**, a Computer Algebra System in pure Python. SymPy can help you conduct detailed analyses of mathematical models. The chapter ends with a short introduction to **Sage**, another Python-based system for computational mathematics.

* [15.1. Diving into symbolic computing with SymPy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/01_sympy_intro.ipynb)
* [15.2. Solving equations and inequalities](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/02_solvers.ipynb)
* [15.3. Analyzing real-valued functions](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/03_function.ipynb)
* [15.4. Computing exact probabilities and manipulating random variables](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/04_stats.ipynb)
* [15.5. A bit of number theory with SymPy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/05_number_theory.ipynb)
* [15.6. Finding a Boolean propositional formula from a truth table](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/06_logic.ipynb)
* [15.7. Analyzing a nonlinear differential system: Lotka-Volterra (predator-prey) equations](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/chapter15_symbolic/07_lotka.ipynb)
* 15.8. Getting started with Sage
* [Full list of references](https://github.com/ipython-books/cookbook-code/blob/master/references/chapter15_symbolic.md)

