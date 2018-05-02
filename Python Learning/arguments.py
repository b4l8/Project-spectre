#! /usr/bin/env python

def print_params(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar

print_params(1,2,3,4,5,6,foo = 1,bar = 2)
