#! /usr/bin/env python

try:
    x = input('x=?')
    y = input('y=?')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero"
except TypeError:
    print "input not a number"
    
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except (ZeroDivisionError,TypeError,NameError):
            if self.muffled:
                print 'Input error'
            else:
                raise
cal = MuffledCalculator()
print cal.calc('10/2')
#print cal.calc('10/0')

cal.muffled = True
cal.calc('10/0')

