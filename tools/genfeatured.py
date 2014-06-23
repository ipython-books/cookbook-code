import sys
import os
import os.path as op
import re

from util import get_recipe_number, get_recipe_name

current_dir = op.dirname(os.path.abspath(__file__))
code_dir = op.join(current_dir, '../')
featured_dir = op.join(code_dir, 'featured/')
site_dir = op.join(current_dir, '../../ipython-books.github.io')

index_path = op.join(site_dir, 'index.html')

def get_title(notebook_filename):
    return get_recipe_name(op.join(featured_dir, notebook_filename))

def get_snippet(name):
    with open(index_path, 'r') as f:
        contents = f.read()
    start = contents.index('<!-- BEGIN {0} -->'.format(name))
    end = contents.index('<!-- END {0} -->'.format(name))
    return contents[start:end]
    
def get_navbar():
    return get_snippet('NAVBAR')
    
def get_footer():
    return get_snippet('FOOTER')
    
NAVBAR = get_navbar()
FOOTER = get_footer()
    
def transform_featured(notebook_filename):
    notebook_filename = op.basename(notebook_filename)
    number = int(notebook_filename[:2])
    notebook_basename = op.basename(notebook_filename)
    input_path = op.realpath(op.join(featured_dir, notebook_filename))
    output_path = op.realpath(op.join(site_dir, 
        'featured-{0:02d}'.format(number)))
    
    # Get the recipe's title.
    title = get_title(input_path)
    
    # Generate the nbconvert command.
    command = ('ipython nbconvert {f} --to html '
               '--template featured.tpl --output {of}').format(
                    f=input_path,
                    of=output_path)
    os.system(command)
    
    output_path += '.html'
    # Replace the templates: title, navbar, footer.
    with open(output_path, 'r') as f:
        contents = f.read()
    contents = contents.replace('%TITLE%', title)
    contents = contents.replace('%NAVBAR%', NAVBAR)
    contents = contents.replace('%FOOTER%', FOOTER)
    with open(output_path, 'w') as f:
        f.write(contents)
    
def main():
    transform_featured(sys.argv[1])
    
if __name__ == '__main__':
    main()
    