#! /usr/bin/env python

#list version
'''
names = ['Alice','Beth' ,'Cecil' ,'Dee' ,'Earl']
numbers = ['2341','9012','3315','0142','5551']

o = raw_input('looking for:')
print numbers[names.index(o.title())]

'''
#dictionary demo
#nested dictionary demo
phonebook={'Alice':{'phone':'2341',
			'addr':'Aoo rue 23'},
	'Beth':{'phone':'9012',
			'addr':'bff street 45'},
	'Cecil':{'phone':'3315',
			'addr':'Cgg avenue 56'},
	'Dee':{'phone':'0142',
			'addr':'Dkk boulevard 78'},
	'Earl':{'phone':'5551',
			'addr':'Ehh drive 90'}
}

labels = {
	'phone':'phone number',
	'addr':'address'}

o = raw_input('looking for:')

#real dirty code
if o.title() in phonebook: print "%s's %s is %s,%s is %s" % \
	(o,labels['phone'],phonebook[o.title()]['phone'],\
	labels['addr'],phonebook[o.title()]['addr'])

#take use of formating to output
print 'test conversion specifier %% on dictionary :'
#template 1: use dirctionary as % format spicifier
template1 = "Template1: The required phone number is %(phone)s, address is %(addr)s"
print template1 % phonebook[o.title()]

#template 2: use method format
require = raw_input("require for ?")
template2 = "Template2: The required %s is {0[%s][%s]}" % (labels[require],o.title(),require)
print template2.format(phonebook)

