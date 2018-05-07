#! /usr/bin/env python

__metaclass__=type

class FooBar:
    def __init__(self,value = 42):
        self.var = value


# auto construction without initialization
f = FooBar()
print f.var
f = FooBar('Constructor with a default value but assigned this value')
print f.var


# in fact we also have an auto destructor called __del__, but it is unable to know when it will be called .
# so try not using it

# now try something done in the previous excercises

class A:
    def hello(self):
        print "hello ,I'm A"

"""class B:
    pass
"""
class B(A):
    def hello(self):
        print "hello ,I'm B"

a = A()
b = B()

a.hello()
b.hello()

class Bird():
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaaaaaah'
            self.hungry = False
        else:
            print 'No, thanks!'
            
            
bb= Bird()
bb.eat()
bb.eat()#base class 

class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
sb = SongBird()
sb.sing()
#sb.est() for current version there is error because __init__ function overwritten there is no hungry() in the class songbird

# solution 1 : call the unbounded superclass constructor
class SongBird1(Bird):
    def __init__(self):
        Bird.__init__(self)# here is the diff
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
        
sb1 = SongBird1()
sb1.sing()
sb1.eat()
sb1.eat()        

# solution 2 : super
# cmparing with solution 1, super method can collect all the superclass consturctor at the sametime
class SongBird2(Bird):
    def __init__(self):
        super(SongBird2,self).__init__()# here is the diff
        self.sound = 'Squawk'
    def sing(self):
        print self.sound
        
sb2 = SongBird2()
sb2.sing()
sb2.eat()
sb2.eat()  



# basic protocol for sequence and map:

"""
__len_(self) : return number of element from a set
__getitem__(self,key): value correspond to the key
__setitem__(self,key,item): 
__delitem__(self,key):
"""
"""
for a sequence if key negative, it counts from the end to the top
key error -> TypeError
index out of ->range IndexError
"""
#demo 1: a sequence infinite
def checkIndex(key):
    if not isinstance(key,(int,long)): raise TypeError
    if key<0:raise IndexError

class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start = start
        self.step = step
        self.changed = {}
    def __getitem__(self,key):
        checkIndex(key)
        try:return self.changed[key]
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self,key,value):
        checkIndex(key)
        self.changed[key] = value
            
s = ArithmeticSequence(1,-5)
print s[4]
s[4] = 2
print s[4]

#demo 2: a list with an access counter

class CounterList(list):
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter = 0
    def __getitem__(self,index):
        self.counter += 1
        return super(CounterList,self).__getitem__(index)
cl = CounterList(range(10))
print cl
print cl.counter
print cl[5]+cl[2]
print cl.counter


#for more detail ref: www.python.org/doc/ref/specialnames.html
