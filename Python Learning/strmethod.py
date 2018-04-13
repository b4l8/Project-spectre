#! /usr/bin/env python

#find()
s= 'ABCDEFGabcdefg01234567:!sqfQ '
print s.find('abc'),s.find('!'),s.find('LL')
#join()
seq = ['1','2','3','4','5']
sep = '+'
dirs = '','usr','bin','env'
r1=sep.join(seq)
print r1,'\\'.join(dirs)
#split()
print r1.split('+'),'Using the Default'.split()
#lower()
print s.lower()
#title()
titlize ="we'll found that title() don't work very well:"
print titlize.title()
from string import capwords
titlize2 = capwords(titlize)
print titlize2

#replace()
print 'Theez eez a test'.replace('eez','is')
#translate()
"""1. make translate table : contains 256 terms
	can manual but use maketrans OK
   2. Use translate table	
"""
from string import maketrans
table = maketrans('cs','kz')
#lets see whats in table
#print table
#print maketrans('','')
print 'This is an incredble test'.translate(table)
print 'The 2nd arg of translate can chose char to remove'.translate(table,' es')

#strip() 
"""remove FORMAT by 2 sides"""
print '          internal whitespace is kept       '.strip()
print '*****SPAM * FOR * EVERYONE!!!! *** '.strip(' *!')
'''
import string
print string.digits(s),
print string.letters(s)
print string.lowercase(s)
print string.printable(s)
print string.punctuation(s)
'''
