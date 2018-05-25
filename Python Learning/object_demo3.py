#! /usr/bin/env python

__metaclass__=type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height= 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize) 
    #size can be used like a normall property.don't need to consider how it works
    #property(fget,fset,fdel,doc)


#-------without property
r = Rectangle()
r.width = 10
r.height = 5
print r.getSize()
r.setSize((150,100))
print r.getSize()
#--------with property
print r.size
r.size = 15,10
print r.size

# decorator:
class MyClass:
    def smeth():
        print 'this is a static method'
    smeth = staticmethod(smeth)
    
    def cmeth(cls):
        print 'This is a class method of',cls
    cmeth = classmethod(cmeth)
MyClass.smeth()
MyClass.cmeth()
class MyClass1:
    @staticmethod
    def smeth():
        print 'this is a static method'
    
    @classmethod
    def cmeth(cls):
        print 'This is a class method of',cls

MyClass1.smeth()
MyClass1.cmeth()


# intercept:
"""
__getattribute__(self,name)  called when 'name' being accessed
__getattr__(self.name)  called when 'name' being accessed and when the object dost not have a corresponding property
__setattr__(self,name,value)  called when trying to assigne value on 'name'
__delattr__(self,name) called when trying to del 'name'
"""


class Rectangle2():
    def __init__(self):
        self.width = 0
        self.height =0
    def __setattr__(self,name,value):
        if name == 'size':
            self.width,self.height = value
        else : 
            self.__dict__[name] = value
    def __getattr__(self,name):
        if name == 'size':
            return self.width,self.height
        else:
            raise AttributeError
            
R = Rectangle2()
R.size = 2,5
print R.size
R.height = 15
print R.size,R.width


# iterator protocol
# __iter__ implements the next method
"""__iter__ in fact return a iterator, a iterator is an object with a 'next' method.
when 'next' called , iterator return the next value. 
"""

class Fibs:
    "if implements by list, it will be infinite"
    def __init__(self):
        self.a=0
        self.b=1
    def next(self):
        self.a, self.b = self.b,self.a+self.b
        if self.a>100000:raise StopIteration # to enable list(fibs). without this, a infinite list will overrun the memory
        return self.a
    def __iter__(self):
        return self
        
fibs = Fibs()
for f in fibs:
    print f,
    if f>1000:
        break
fibs.__init__()
# Attention : list on an infinite iterator will be extramely dangerious
print list(fibs)


# Generator protocol
# any line contain 'yield' cmd: each time yield a new value, function freezed until next activated
# 1. a nested list
nested = [[1,2],[3,4],[5,6],[7,8]] 
g = (i**2 for i in range(8))
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
# 2. see the flatten is freezed after generate 1 value, and resume next time.

for num in flatten(nested):
    print num 

print g.next()
print g.next()
print list(g)

# a recursion generator demo
# Attention : don't iterate on a str object. this recursion will never end because the 1st element of a string is a string len=1. it will ref to itself infinitly
def flatten2(nested):
    try:
        try: nested+'' # add support to string
        except TypeError:pass #if TypeError (not string), pass
        else: raise TypeError #if string,raise typeError: =>yield the string
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested
        
print list(flatten2([[[1],2],3,4,[5,[6,7]],8]))
print list(flatten2(['foo',['bar',['1234']]]))

# Generator = Generator function + Generator Iterator
# generator function = def xxxxxxx with yield
# generator function returns an iterator


# demo : Generator method -> send (there is other method : -> throw -> close)

def repeator(value):
    while True:
        new = (yield (value+1))
        if new is not None: value = new

r = repeator(42)
print r.next() # Attention : send can only be used after the 1st yield. when the generator at the suspended condition
# reinput value : send value to generator
r.send(10)
print r.next()
print r.next()
print r.next()
print r.next()
print r.next()




