import os
from glob import glob

def generate_cmd(name):
    return 'pandoc '+name+'.md -s -o '+name+'.pdf'

md_files = glob('*md') + glob('*/*md') + glob('*/*/*md')

for md in md_files:
    name = md.split('.md')[0]
    os.system(generate_cmd(name))
