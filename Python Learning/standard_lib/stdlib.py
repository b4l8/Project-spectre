#! /usr/bin/env python

### sys
"""
argv            || kind of command line arguments including script name
exit([arg])     || exit current program. passing a return val or bug message 
modules         || mapping a module name on to the module charged
path            || string list , every string is a path
platform        || a string telling the current platform 
stdin           || file stream object 
stdout          || file stream object 
stderr          || file stream object 
"""

import sys
args = sys.argv[1:]
args.reverse()
print ' '.join(args)
# test by running "stdlib.py this is a test"

### os
"""
give access to system service, here is some useful func/variable

environ         || mapping environment variable. ie: os.everion['PYTHONPATH']
system(command) || run extern cmd in a sub shell
sep             || seperator
pathsep         || path seperator
linesep         || string seperator (UNIX: '\n',MAC: '\r', windows: '\r\n')
urandom(n)      || return n bytes encrypted strong random data
"""
# import os
#os.system('/usr/bin/google-chrome')
# Note: for windows ,it is better using "os.startfile(PATH)" because of the problem of support on path string
# Tip , use webbrowser module : webbrowser.open('http://www.python.org') 


### fileinput

"""
when calling script using filename as args:
python somescript.py file1.txt file2.txt file3.txt
also, using function input in the module can do the same thing

input([files[,inplace[,backup]]])   || traverse lines in multiple streams 
filename()                          || return current filename
lineno()                            || return current line N0,it will not reset when changing file
filelineno()                        || return line N0 in current file ,reset when changing file 
isfirstline()                       || True if is the first line of current file
isstdin()                           || True if current file is sys.stdin
nextfile()                          || close current file goto next file, skipped line won't count
close()                             || close the whole file chain, finish file iteration

"""
# ref commentlines.py 4example

### Data structure : set,  heap  and double-ended queue(deque)
"""
set : need not import. created by an iterable object, no order
union([set])         or  "|"
intersection([set])  or  "&"
issubset([set])      or  "<="
issuperset([set])    or  ">="
difference([set])    or  "-"
symmetric_difference([set])  or "^"
copy()
"""
a = set([1,2,3])
b = set([2,3,4])
print a.union(b) #or
print a|b 

# Note : set is variable. so it can't be key to a dic. set item can only be const
#        so set element can't be a set too. 
# Note 2: but we can convert a set into an copy with type "frozenset" , this is all ok


"""
heap: import heapq
heappush(heap,x)        || push in 
heappop(heap)           || pop out (smallest)
heapify(heap)           || list to heap
heapreplace(heap,x)     || pop smallest, x push in
nlargest(n,iter)        || return nth largest in the iter
nsmallest(n,iter)       || return nth smallest in the iter

"""

from heapq import *
from random import shuffle
data = range(20)
shuffle(data)
print data
heapify(data)
print data


"""
deque : from collection import deque
deque(iter)
append(x)
appendleft(x)
pop()
popleft()
rotate(n)
"""

### time : a tuple with 9 integers
"""
index   ||  segmentation    || value
0       ||  year            || year int 
1       ||  month           || 1-12
2       ||  day             || 1-31
3       ||  hour            || 0-23
4       ||  minute          || 0-59
5       ||  second          || 0-61
6       ||  week            || 0-6
7       ||  day of year     || 1-366
8       ||  summer time     || 0,1 or -1
"""
"""
asctime(tuple)                  || time tuple to string
localtime(secs)                 || sec value to time tuple, convertion by local time
gmtime(secs)                    ||
mktime(tuple)                   || time tuple to local time
sleep(secs)                     || sleep
strptime(string(,format))       || time string to time tuple
time()                          || current time UTC
"""


### random :

"""
random()                        || random 0-1
getrandbits(n)                  || longint type return a n bit binary num
uniform(a,b)                    || random value(float) between a,b 
randrange([start],stop,[step])  || random int in range(condition)
choice(seq)                     || random choice
shuffle(seq[,rand])             || shuffle
sample(seq,n)                   || random choice a number of samples
"""
from random import *

val = getrandbits(16) # a 16 bits rand
print val


values = range(1,11)+'Jack Queen King'.split()
suits  = 'diampnds clubs hearts spades'.split()

deck =['%s of %s' %(v,s) for v in values for s in suits]
## create a deck of card
for item in deck:
    print item
shuffle(deck)
#while deck:
 #   raw_input(deck.pop())


###  shelve :
""" 
 open(name) : return a shelf object, can be used as a dic. (key must be str)
 close() 
"""
import shelve
s = shelve.open('shuffled_deck.dat')
s['deck'] = deck
s['deck'].append('clown')
print s['deck']
# here 'clown' not appended in file. because the new appended list is in the copy but not the original  , the correct way is :
temp = s['deck']
temp.append('clown')
s['deck'] = temp # re-assign 
print s['deck']
