#! /usr/bin/env python

import sqlite3,sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]
print query
curs.execute(query)
names = [f[0] for f in curs.description]

for row in curs.fetchall():
    for pair in zip(names,row):
        print '%s:%s'% pair
    print 
    
    
# food_query.py "kcal<=100 AND fiber >=2 ORDER BY sugar"
