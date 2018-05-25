#! /usr/bin/env python                   #  1
                                         #  2
import fileinput                         #  3
                                         #  4
for line in fileinput.input(inplace=True): #  5
    line = line.rstrip()                 #  6
    num = fileinput.lineno()             #  7
    print '%-40s # %2i' % (line,num)     #  8
                                         #  9
# try stdlib.py greeting.py              # 10
