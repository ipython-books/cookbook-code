IPython Cookbook: the code
==========================

This repository contains all the code of the [IPython Cookbook](https://ipython-books.github.io), the definitive guide to high-performance scientific computing and data science in Python (Cyrille Rossant, Packt Publishing).

I will fill this repository progressively over the next few months, [follow me](https://twitter.com/cyrillerossant) for being kept informed!


## Structure of the repository

The structure of the repo is the following:

```
notebooks/                      all notebooks with the code of all examples
    chapter-01-intro/           all notebooks of chapter 1
        recipe-01-intro.ipynb
        ...
    chapter-02-practices/       all notebooks of chapter 2
    ...
    extra/                      extra code example that did not make it in the book
    guests/                     guest recipes
featured/                       featured complete recipes with all text and code
    01-featured-recipe.ipynb
    ...
references/
    chapter-01-intro.md         contains a curated list of references
    ...
tools/                          contains various build scripts
    build.py
    ...
```

All the code is in the `notebooks/` folder. A selection of recipes, called *featured recipes**, are in `featured/`. They contain entire recipes (text with the explanations, the code, the figures).


## Installation

You need Python 2 or 3 and a bunch of scientific modules for the code examples. The most important modules you will need are: IPython 2+, NumPy, SciPy, Pandas, matplotlib. Many recipes that require other modules come with the appropriate installation instructions.

We highly recommend that you use an all-in-one Python distribution like [Anaconda](http://continuum.io/downloads). This distribution comes with an excellent package manager named *conda*. It lets you install easily many modules on most platforms (Windows, Linux, Mac OS X), in 64-bit (recommended if you have a 64-bit OS) or 32-bit.

Anaconda supports either Python 2 or Python 3. If you're not sure, pick Python 3.


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

You are welcome to contribute to this repository. You can use the issue tracker to report any problem. You can also propose a pull request (PR) to fix an error, to add some information, or even add a brand new recipe in the `guest/` folder!


