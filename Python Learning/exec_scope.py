#! /usr/bin/env python

from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
r=sqrt(4)
print r
r2 = scope['sqrt']
print r2
print len(scope),"\n",scope.keys()

scope2 = {'y':3,'x':2}
while True:
    word = raw_input('Enter an arithmetic expression:')
    if word == 'q':
        break;
    r3=eval(word,scope2)
    print 'the answer is %d'%r3



