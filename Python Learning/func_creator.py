#! /usr/bin/env python


def multiplier(factor):
    def multiplyByFactor(number):
	return number*factor
    return multiplyByFactor


by2 = multiplier(2)
by3 = multiplier(3)
print by2(5),by3(5),multiplier(4)(5)

#list:
num_list = map(str,range(10))
print num_list

#filter:
seq = ["foo","x41","qsfqs","?!","!!","****","465"]
def func(x):
	return x.isalnum()

res=filter(func,seq)
print res

#lambda:
res2 = filter(lambda x: x.isalnum(),seq)
print res2

#reduce:

numbers = [x for x in range(100) if x%2==0]
print numbers

sig=reduce(lambda x,y:x+y,numbers)
print sig
