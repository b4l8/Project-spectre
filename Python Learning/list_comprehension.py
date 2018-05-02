#! /usr/bin/env python


list1 = [(x,y) for x in range(5) for y in range(9,0,-3)]
list2 = [x*x for x in range(10) if x%3 == 0 ]

girls = ['alice','bernice','clarice']
boys  = ['chris','arnold','bob']
list3 = [b+'+'+g for b in boys for g in girls if b[0]==g[0]]
print list1,"\n",list2,"\n",list3
