IPython Cookbook
================

This repository contains the recipes of the [IPython Cookbook](http://ipython-books.github.io), the definitive guide to **high-performance scientific computing** and **data science** in Python, by [Dr. Cyrille Rossant](http://cyrille.rossant.net), Packt Publishing, 500 pages, September 2014.

[Follow me on Twitter to get all updates](https://twitter.com/cyrillerossant)


## Featured recipes

A selection of free recipes from the book:

1. [Getting the best performance out of NumPy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/featured/01_numpy_performance.ipynb)
2. [Simulating a physical system by minimizing an energy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/featured/02_energy_minimization.ipynb)
3. [Creating a route planner for road network](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/featured/03_gps.ipynb)
4. [Introduction to machine learning in Python with scikit-learn](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/featured/04_scikit.ipynb)
5. [Simulating a partial differential equation: reaction-diffusion systems and Turing patterns](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/featured/05_turing.ipynb)
6. [Getting started with Vispy](http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/featured/06_vispy.ipynb)
* more coming soon...


## Table of contents

* [See the full table of contents here](toc.md)


## Errata

You can report inaccuracies or errors in the [GitHub issue tracker](https://github.com/ipython-books/cookbook-code/issues). Even better, propose your own corrections by submitting a pull request!

* [See the list of errata here](errata.md)


## Example data

[You will find the data used in the recipes here](https://github.com/ipython-books/cookbook-data).


## Structure of the repository

The structure of the repo is the following:

```
notebooks/                      all notebooks with the code of all examples
    chapter01_tour/             
    chapter02_best_practices/   
    ...
    extra/                      extra code example that didn't make it in the book
    guests/                     guest recipes
featured/                       a selection of complete recipes with all text, figures and code
references/                     a curated list of references about scientific Python programming
tools/                          various building Python scripts
```


## Installation

You need Python 3 (or 2) and a bunch of scientific modules for the code examples, mainly IPython 2.0+, NumPy, SciPy, Pandas, and matplotlib. Many recipes that require other modules come with the appropriate installation instructions.

We highly recommend that you use an all-in-one Python distribution like [Anaconda](http://continuum.io/downloads). This distribution comes with an excellent package manager named *conda*. It lets you install easily many modules on most platforms (Windows, Linux, Mac OS X), in 64-bit (recommended if you have a 64-bit OS) or 32-bit.

The recipes are written for Python 3 first, but they also work with Python 2. Please favor Python 3 over Python 2 if you can.


## Cloning the repository

You need [git](http://git-scm.com/), a distributed versioning system, to download a local copy of this repository. Open a terminal and type:

```
git clone https://github.com/ipython-books/cookbook-code.git
```

This will copy the repository in a local folder named `cookbook-code`.


## Running the examples

Launch the IPython notebook server with:

```
ipython notebook
```

In your browser, go to `127.0.0.1:8888`. You can navigate in the repository and open the notebooks.


## Contribute

You are welcome to contribute to this repository. You can use the issue tracker to report any problem. You can also propose a pull request (PR) to fix an error, to add some information, or even propose a brand new recipe in the `guests/` folder!


