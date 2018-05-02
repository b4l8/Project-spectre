#! /usr/bin/env python

__metaclass__ = type
class Person:
    members = 0
    def init(self):
        Person.members += 1
    def setName(self,name):
        self.name = name
        # self is the objest itself
    def getName(self):
        return self.name
		
    def greet(self):
        print "Hello! I'm %s." % self.name
        
    def __inaccessible(self):
        print "bet you can't see me ..."
        
    def accessible(self):
        print "The secret message is :"
        self.__inaccessible()
        
foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
 
foo.greet()
bar.greet()
print foo.name

foo.accessible()
# in python class, all "__[name]" form are translated into "_[Class name]__[name]"
# names with a "_" in the beginning can't be imported by "*" (be all selected)
foo._Person__inaccessible()

foo.init()
foo.init()
bar.init()
bar.init()
# the variable in the class namespace can be accessible by ALL INSTANCE
print Person.members,foo.members
# but modification on this variable is in the instance itself's scope
foo.members = 'nobady'
print Person.members,foo.members
