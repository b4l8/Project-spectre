#! /usr/bin/env python

# tag adder, 
# support : start tag, paragraph tag , end tag

# cmd example : simple_marker.py <text_input.txt> test_ouput.html

import sys,re

from util import *

print '<html><head><title>...</title><body>'

title = True

for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block) # change *something* to  <em>somthing</em>
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'
print '</body></html>'
