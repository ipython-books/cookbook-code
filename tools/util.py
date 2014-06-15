import re
import urlparse
import json
import os
import sys
import os.path as op

def get_recipe_number(file):
    return int(file[:2])

def get_recipe_name(file):
    # Load notebook.
    with open(file, 'r') as f:
        contents = json.load(f)
    cells = contents['worksheets'][0]['cells']
    for cell in cells:
        if cell.get('cell_type', None) == 'markdown':
            source = cell.get('source', [])
            for _ in source:
                if _.startswith('# '):
                    return _[2:].strip()
      