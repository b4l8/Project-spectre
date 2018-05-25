#! /usr/bin/env python

def hello():
    print "Hello,World!!"


def test():
    print "test : ",
    hello()


if __name__== '__main__':test() # make sure, when import, won't run . but can call test
