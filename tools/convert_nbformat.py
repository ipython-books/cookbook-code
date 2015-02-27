
import re
import json
import os
import sys
import os.path as op

from IPython.nbformat import read, convert, write, validate

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

curdir = op.realpath(op.dirname(os.path.abspath(__file__)))
root = op.realpath(op.join(curdir, '../notebooks'))

def convert_to_v4(path):
    nb = read(path, 3)
    nb_new = convert(nb, 4)

    for cell in nb_new['cells']:
        if cell.get('metadata', {}) == []:
            cell['metadata'] = {}

    nb_new["metadata"] ={
         "kernelspec": {
          "display_name": "Python 3",
          "language": "python",
          "name": "python3"
         },
         "language_info": {
          "codemirror_mode": {
           "name": "ipython",
           "version": 3
          },
          "file_extension": ".py",
          "mimetype": "text/x-python",
          "name": "python",
          "nbconvert_exporter": "python",
          "pygments_lexer": "ipython3",
          "version": "3.4.2"
         }
        }

    validate(nb_new)
    write(nb_new, path)

if __name__ == '__main__':

    for chapter in iter_chapters(root):
        for recipe in iter_recipes(root, chapter):
            file = op.join(root, chapter, recipe)

            if recipe in ('01_notebook.ipynb',
                          '02_pandas.ipynb',
                          '03_numpy.ipynb',):
                continue
            print("converting", file)
            convert_to_v4(file)
