#! /usr/bin/env python

def fibs(num):
    'show the first [num] fibonacci number as asked'
    result = [0,1]
    for i in range(num-2):
         result.append(result[-2]+result[-1])
    return result

x = raw_input('how many items of fibonacci?')
print fibs(int(x))
print fibs.__doc__
print help(fibs)


def init(data):
    '''intialise the data in the dict like format :
    "storage['first'] ={}"
    "storage['middle'] ={}"
    "storage['last'] ={}"'''
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}
storage = {}

def lookup(data,label,name):
    return data[label].get(name)


def store(data,full_name):
    'put new name in the data structure'
    names = full_name.split()
    if len(names) == 2 : names.insert(1,"")
    lables = 'first','middle','last'
    for label,name in zip(lables,names):
        already_there = lookup(data,label,name)
        if already_there:
            already_there.append(full_name)
	else:
	    data[label][name] = [full_name]


init(storage)
store(storage,"magnus lie hetland")
print lookup(storage,'middle','lie')

while True:
    cmd = raw_input("cmd?")
    if cmd == 'q': break
    exec cmd
##try these cmd:
"""print storage
store(storage,'Robin Hood')
store(storage,'Robin Locksley')
ans = lookup(storage,'first','Robin')
print ans
store(storage,'Mr. Gumby')
ans = lookup(storage,'middle','')
print ans
rm """
