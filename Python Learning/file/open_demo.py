#!/usr/bin/env python

from __future__ import with_statement
# python open: 'r' default
"""
r       read
w       write
a       addition
b       binary
+       r/w mode
"""
# to make a cross plateform script, windows newline :\r\n will be auto replaced by \n
# This will cause critical error when dealing binary file, if forget the mode 'b',
# auto replacement of newline will cause error (in fact, this only occurs when cross platform on windows or other plateform). In unix, as newline = \n, nothing will happen. and there is no such error.

# buffering:
"""
0 or False : no buffering
1 or True  : buffer IO stream. Only update data when flush or close ;
             Any value > 1 means the size of buffer. -1 means default size
"""

f = open('somefile.txt','w')
f.write('Hello, ')
f.write('World!')
f.write('\n Write a line')
f.close()

f = open('somefile.txt','r')
print f.read(4)
print f.read()
f.close()

# with statement , no matter it fail or success, file will be closed

with open("somefile.txt") as somefile:
    print somefile.read()




# fictitious function
def process(string):
    print 'Processing: ',string
# read by char
f = open("somefile.txt")
while True:
    char = f.read(1)
    if not char: break
    process(char)
f.close()

# read by line
f = open("somefile.txt")
while True:
    line = f.readline(1)
    if not line: break
    process(line)
f.close()

# or use fileinput
import fileinput
for line in fileinput.input("somefile.txt"):
    process(line)
    
# Or , in fact ,a file is iterable
f = open('somefile.txt')
for line in f:
    process(line)
f.close()

f1 = open('somefile.txt')
f2 =  open('somefile.txt')
lines = list(f1)
print lines
line1,line2 = f2
print line1,line2
