#! /usr/bin/env python

import sys
sys.path.append('..')
import hello

import hello 
# we'll see hello.py run only once , if we do want to import again ,try:

hello = reload(hello) # removed in p3.0

import sys,pprint
 
pprint.pprint(sys.path)
sys.path.append('.')
import greeting
greeting.test()


import package
import package.colors
from package import shapes
# dir cmd ,helo us find the files in "copy"
import copy
print [n for n in dir(copy) if not n.startswith('_')]
# or
print copy.__all__
# what is [__all__] ?
# it defines a list of all public interface of the module
# so when using "from copy import * ", we got the function in the list
# without defining the __all__ list, import * will output every function that not begin with '_'

print help(copy.copy)
print copy.__file__
