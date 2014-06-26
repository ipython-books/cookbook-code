# 2. Best practices in Interactive Computing

Full list of references in Chapter 2 of the [IPython Cookbook](http://ipython-books.github.io), the definitive guide to high-performance scientific computing and data science in Python, by Dr. Cyrille Rossant, Packt Publishing, 400 pages, 2014.

## Python 2/Python 3

* [What's new in Python 3?](http://docs.python.org/3.3/whatsnew/3.0.html).
* [An excellent free book about porting code to Python 3, by Lennart Regebro](http://python3porting.com).
* [Official recommendations about Python 2/Python 3 compatibility](http://docs.python.org/3/howto/pyporting.html).
* [`2to3` module to convert Python 2 code to Python 3](http://docs.python.org/2/library/2to3.html).
* [`six` compatibility module](http://pythonhosted.org/six/).
* [Official wiki page about the Python 2/Python 3 question](http://wiki.python.org/moin/Python2orPython3).
* [Python 3 questions and answers, by Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html).
* [*"Ten awesome features of Python that you can't use because you refuse to upgrade to Python 3"*, a presentation by Aaron Meurer](http://asmeurer.github.io/python3-presentation/slides.html).
* [Using the `__future__` module when writing compatibility code](http://docs.python.org/2/library/__future__.html).
* [Key differences between Python 2 and Python 3](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).


## Integrated Development Environments for Python

* [PyDev for Eclipse](http://pydev.org).
* [Spyder, an open source IDE](http://code.google.com/p/spyderlib/).
* [PyCharm](http://www.jetbrains.com/pycharm/).
* [PyTools for Microsoft Visual Studio on Windows](http://pytools.codeplex.com).
* [PyScripter](http://code.google.com/p/pyscripter/).
* [IEP, the Interactive Editor for Python](http://www.iep-project.org).


## Git

* [msysgit: Git for Windows](http://msysgit.github.io).
* [TortoiseGit](http://code.google.com/p/tortoisegit/).


## Hosted Git Services

* [GitHub](http://github.com).
* [BitBucket](http://bitbucket.org).
* [Google Code](http://code.google.com).
* [Gitorious](http://gitorious.org).
* [Sourceforge](http://sourceforge.net).


## Learning Git

* [GitHub help](http://help.github.com).
* [Pro Git book](http://git-scm.com).
* [Hands-on tutorial](http://try.github.io).
* [Git Guided Tour](http://gitimmersion.com).
* [GitHub Git tutorial](http://git-lectures.github.io).
* [Atlassian Git tutorial](http://www.atlassian.com/git).
* [CodeSchool's online course](http://www.codeschool.com/courses/try-git).
* [Git tutorial by Lars Vogel](http://www.vogella.com/tutorials/Git/article.html).
* [Git tutorial for scientists](http://nyuccl.org/pages/GitTutorial/).

## Git workflows

* [A popular but complex Git flow](http://nvie.com/posts/a-successful-git-branching-model/).
* [A simpler workflow, used by GitHub](http://scottchacon.com/2011/08/31/github-flow.html).
* [Different Git workflows](http://www.atlassian.com/git/workflows).
* [Learn Git branching](http://pcottle.github.io/learnGitBranching/).
* [The Git workflow recommended on the NumPy project (and others)](http://docs.scipy.org/doc/numpy/dev/gitwash/development_workflow.html).
* [A post on the IPython mailing list about an efficient Git workflow, by Fernando Perez](http://mail.scipy.org/pipermail/ipython-dev/2010-October/006746.html).


## Good practices

* [The Python Cookbook, by David Beazley, a must-read with many advanced recipes for Python 3](http://shop.oreilly.com/product/0636920027072.do).
* [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/).
* [PEP8 rules](http://www.python.org/dev/peps/pep-0008/).
* [PyLint, a static analysis tool](http://www.pylint.org).
* [Design patterns in Python](http://github.com/faif/python-patterns).
* [Design patterns on Wikipedia](http://en.wikipedia.org/wiki/Software_design_pattern).
* [Coding standards of Tahoe-LAFS](http://tahoe-lafs.org/trac/tahoe-lafs/wiki/CodingStandards).
* [*"How to be a great software developer"*, by Peter Nixey](http://peternixey.com/post/83510597580/how-to-be-a-great-software-developer).
* [*"Why you should write buggy software with as few features as possible?"* a talk by Brian Granger](http://www.youtube.com/watch?v=OrpPDkZef5I).


## Packaging

* [The Hitchhiker’s Guide to Packaging](http://guide.python-distribute.org).
* [Python Packaging User Guide](http://python-packaging-user-guide.readthedocs.org).
* [Conda](http://conda.pydata.org).


## Reproducibility

* [*"An efficient workflow for reproducible science"*, a talk by Trevor Bekolay](http://bekolay.org/scipy2013-workflow/).
* [*"Ten Simple Rules for Reproducible Computational Research"*, Sandve et al., PLoS Computational Biology, 2013](http://dx.doi.org/10.1371/journal.pcbi.1003285).
* [Konrad Hinsen's blog](http://khinsen.wordpress.com).

### Tools

* [Markdown, a simple markup language](http://daringfireball.net/projects/markdown/).
* [Sphinx](http://sphinx-doc.org).
* [Figshare for storing binary research data online](http://figshare.com).
* [Datadryad for storing binary research data online](http://datadryad.org).
* [joblib, a must-have tool for interactive computing](http://pythonhosted.org/joblib/).
* [ipycache, providing a `%%cache` magic in IPython](http://github.com/rossant/ipycache).
* [AutoIt to automate GUI actions](http://www.autoitscript.com/site/autoit/).
* [AutoHotKey to create automation scripts on Windows](http://www.autohotkey.com).


## Unit testing

* [Nose, a unit testing package for Python](http://nose.readthedocs.org/en/latest/testing.html).
* [Test-driven development](http://en.wikipedia.org/wiki/Test-driven_development).
* [*"Untested code is broken code"*, by Martin Aspeli](http://www.deloittedigital.com/eu/blog/untested-code-is-broken-code-test-automation-in-enterprise-software-deliver).


## Test coverage

* [coverage.py, a Python module by Ned Batchelder](http://nedbatchelder.com/code/coverage/).
* [coveralls.io, a test coverage tool](http://coveralls.io).


## Continuous integration

* [Documentation of Travis CI in Python](http://about.travis-ci.org/docs/user/languages/python/).


## Debugging

* [WinPdb, a graphical debugger](http://winpdb.org).


