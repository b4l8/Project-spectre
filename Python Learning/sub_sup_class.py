#! /usr/bin/env python

class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
        
        
class SPAMFilter(Filter): #SPAMFilter is a subclass of Filter
    def init(self):
        self.blocked = ['SPAM']



# Filter actually do nothing,it is a base class:
f = Filter()
f.init()
print f.filter([1,2,3])
# In SPAMFilter: redifine the init() so that block 'SPAM'; but don't need to redifine the filter()
s = SPAMFilter()
s.init()
print s.filter(['SPAM','SPAM','SPAM','eggs','SPAM','bacon','SPAM','SPAM'])

# check if subclass
print issubclass(SPAMFilter,Filter)
# check base class
print SPAMFilter.__bases__
# check class
print s.__class__
# check if instance
print isinstance(s,SPAMFilter) ,isinstance(s,Filter)

# demonstration of multiple base class
class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)
    def talk(self):
        print 'Calculator saying: there is nothing!'
class Talker:
    def talk(self):
        print 'Hi,the value is :',self.value

# attention : when multiple iniheritance , the former method will shadowing the same name behind
class TalkingCalculator(Calculator,Talker):
    pass
    
tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

# check if have attr

print hasattr(tc,'talk'), hasattr(tc,'fnord')
print callable(getattr(tc,'talk',None)) # in 3.0 , replaced by hasattr(x,'__call__')

print tc.__dict__,Calculator.__dict__
