# Beginners instructions for installing Python

**We only support the Anaconda distribution, although other Python distributions should work too.**

In this *work-in-progress* document, we give very detailled instructions about how to install a full scientific Python distribution. This document targets beginners, and tackles things such as using the command-line interface, installing Anaconda, etc. These instructions are sometimes hard to find, scattered across many websites, blog posts, and posts on support mailing lists. Eventually, you'll find here the very minimum you need to know.

This document aims at being maintained by the community: please propose a Pull Request if an information is missing.


## Overview

Anaconda is a program created by Continuum Analytics. It lets you install a Python distribution with many scientific packages like NumPy, SciPy, IPython, matplotlib, and many others. Anaconda also comes with a packaging tool named conda. This tool lets you maintain, install, and update your Python packages. It is actually more general than that, in that it can deal with any non-Python binary package.


## Things to know

You need to know/learn, several things before you start:

* The system terminal, or command-line interface.
* Git, a version control system.


### The terminal

#### Windows

Use Powershell.


#### Linux

TODO

#### Mac OS X

TODO


### Git

Not strictly required, but highly recommended if you want to use obscure packages, or if you start to write significant amount of code.

TODO:

* Installing git...
* git bash...
* git GUI...


### Environment variables and system paths

TODO


## Installing Anaconda

Once you're relatively confortable with the terminal and git, you can install Anaconda, a Python distribution.


### Windows

* Install Anaconda for Windows with Python 3.x (the latest is 3.4 in Sept. 2014).
* Don't install Anaconda with admin rights: check "Just for me" in the installer.
* Install in a path like `c:\anaconda`.
* You'll be able to install Python 2.x in a separate conda environment.
* **If you use Powershell**, you need to [use customized activate/deactivate scripts](https://github.com/Liquidmantis/PSCondaEnvs.git). Clone the repository, and copy them in `c:\anaconda\scripts` or similar.


### Linux

TODO


### Mac OS X

TODO



## Using Anaconda

### The basics


## Environments

Anaconda lets you maintain various isolated environements. You can switch to any environment at any time from the command-line.

### Get the list of installed environments

`conda info -e`


### Switch to another environment

* On Windows: `activate myenv`
* On another OS: `source activate myenv`


### Installing Python 2.x side-by-side with the default Python 3

* Run the following command:

  `conda create -n py27 python=2.7.8`
  `(press `f` if you have a WARNING)
  
* You'll have no package in this new environment. Make sure to install **pip**!

  `conda install pip`
  `conda update pip`


## Running Python, IPython, and the IPython notebook



## Using a code editor



## Installing new packages

* `conda install mypackage`
* If that doesn't work, it needs that there is no conda package for this Python module. There are solutions.
* **Important**: make sure pip is installed in the currently activated environment with `conda install pip`.
* Then you can try to use pip: `pip install mypackage`.


