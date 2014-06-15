"""Generate table of contents with links to nbviewer."""

import re
import urlparse
import json
import os
import sys
import os.path as op

from util import get_recipe_number, get_recipe_name

CHAPTER_NAMES = [
    'A Tour of Interactive Computing with IPython',
    'Best practices in Interactive Computing',
    'Master the Notebook',
    'Profiling and Optimization',
    'High-Performance Computing',
    'Advanced Visualization',
    'Statistical Data Analysis',
    'Machine Learning',
    'Numerical Optimization',
    'Signal Processing',
    'Image and Audio Processing',
    'Deterministic Dynamical Systems',
    'Stochastic Dynamical Systems',
    'Graphs and Geometry',
    'Symbolic and Numerical Mathematics',
]

def get_chapter_number(dir):
    return int(op.basename(dir)[7:9])
      
def get_chapter_name(number):
    return CHAPTER_NAMES[number-1]
      
def iter_chapters(root):
    for chapter in sorted([_ for _ in os.listdir(root) 
                            if _.startswith('chapter')]):
        yield chapter

def iter_recipes(root, dir):
    files = sorted([_ for _ in os.listdir(op.join(root, dir))
        if re.match(r'\d{2}\_[^.]+\.ipynb', _)])
    for file in files:
        yield file

def yield_chapter_toc(root):
    for chapter in iter_chapters(root):
            number = get_chapter_number(chapter)
            chapter_name = get_chapter_name(number)
            yield chapter, '### Chapter {number}: {name}\n\n'.format(number=number, 
                                                            name=chapter_name)
        
def yield_recipe_toc(root, chapter):
    for recipe in iter_recipes(root, chapter):
        file = op.join(root, chapter, recipe)
        recipe_name = get_recipe_name(file)
        url = urlparse.urljoin(urlbase, chapter + '/' + recipe)
        yield '* [{recipe_name}]({url})\n'.format(
            recipe_name=recipe_name,
            url=url,
        )
        
curdir = op.realpath(op.dirname(os.path.abspath(__file__)))
root = op.realpath(op.join(curdir, '../notebooks'))
urlbase = "http://nbviewer.ipython.org/github/ipython-books/cookbook-code/blob/master/notebooks/"

def write_toc(root, f=sys.stdout):
    with f:
        for chapter, chapter_toc in yield_chapter_toc(root):
            f.write(chapter_toc)
            for recipe_toc in yield_recipe_toc(root, chapter):
                f.write(recipe_toc)
            f.write('\n\n')

if __name__ == '__main__':
    write_toc(root, open('toc.md', 'w'))
    
    # for chapter, chapter_toc in yield_chapter_toc(root):
        # print(chapter_toc)
    