#! /usr/bin/env python

#### full list of regular expression ; https://docs.python.org/2/library/re.html?highlight=regular

## wildcard : '.' = one any char
"""
when using it 'python.org' == 'pythonzorg' , NOT GOOD! 
escape it : 'python\\.org'  no problem
"""
## character set 
"""
'[pj]ython' == 'python','jython'
'[^abc]' == char except for a,b,c
'[a-zA-Z0-9]' all alphbet and number
"""
## subparttern
"""
'p(ython|erl)' == 'python','perl'
"""
## optional item
"""
r'(http://)?(www\.)?python\.org' :
'http://www.python.org'
'http://python.org'
'www.python.org'
'python.org'

attention here -------> escape '.'
               -------> use original string r'xxx', so that no need to use double \
               -------> every optional sub mode in ()
               -------> optional sub mode independent to each other
"""
"""
optional 
(pattern)?:         pattern 0 or once
(pattern)*:         pattern 0 or multiple
(pattern)+:         pattern 1 or multiple
(pattern){m,n}:     pattern repeat m-n times
"""
"""
r'w*\.python\.org' :
.python.org
ww.python.org
www.python.org
wwwwwwwwww.python.org
"""
# top or end match
"""
top:
'^ht+p' : 'http://python.org' 'httttttttp://python.org' but don't match www.http.org
end:
'org$'
"""

####################################################################################

# re  module:
"""
compile(pattern[,flags])            || create pattern into reg-exp object ,this object can be useful
search(pattern,string[,flags])      || Return True ,if find first match string/sub-string
match(pattern,string[,flags])       || Try match pattern at the begin of string. match == True
split(pattern,string[,maxsplit=0])  || split string, can use any pattern u want to 
findall(pattern,string)             || 
sub(pat,repl,string[,count=0])      || 
escape(string)                      || out put escaped string
"""
import re
some_text = 'alpha, beta,,,,,,,,gamma      delta'
print re.split('[, ]+',some_text) # pattern : , or space, any length >=1
print re.split('/(/)','//usr//bin//python') # char in (), will be put into splited strings


pat = '[a-zA-Z]+'
text = '"Hm...Err--are you sure?" he said,souding insecure.'
print re.findall(pat,text) # find all words

pat = '{name}'
text = 'Dear {name}...'
print re.sub(pat,'Mr.Gumby',text) # use repl, to replace all pattern

print re.escape('www.python.org')


###################################################################################

# re matchobject:
"""
group([group1,...])     || get matchobject of given subparttern/group
start([group])          || return start index of given group 
end([group])            || return end of given group 
span([group])           || return (start,end) tuple of given group 
"""


m = re.match(r'www\.(.*)\..{3}','www.python.org')
# pattern = www. + (0-n)x char +.+3xchar
# def a group like : "There (was a (wee) (cooper)) who (lived in Fyfe)"
#                   then it contains group :
"""
                0 (the whole string) 
                1 (sub1) was a wee cooper
                2 (sub2) wee
                3 (sub3) cooper
                4 (sub4) lived in Fyfe
""" 
print m.group(1) # group 0 is 'www.python.org', group1 is 'python'
print m.start(1) # 4          '01234
print m.end(1)   # 10 <---    '0123456789    <----- it return index of end +1, good for slice a string
print m.span(1)
print 'www.python.org'[m.start(1):m.end(1)] # explain the things 

###############################################################################

# write something easy to read:
"""emphasis_pattern = r'\*([^\*]+)\*'"""
emphasis_pattern = re.compile(r'''
        \*          # Beginning emphasis tag -- an asterisk
        (           # Begin group
        [^\*]+      # capture anything except for an asterisk
        )           # End group
        \*          # Ending emphasis tag
        ''',re.VERBOSE) # VERBOSE: allow us to add space,tab,newline,etc into pattern, They will be ignored unless they are escaped.
        # very useful example when trying to add comment
m1 = re.match(emphasis_pattern,'*world*!') # Attenstion,match counts from the beginning. can't search in the middle 
print m1.group(1)  
print re.sub(emphasis_pattern,r'<em>\1</em>','Hello,*world*!')
# sub(pat,\\n,string) : group1 pattern replacement
# in this example: matched group 0 = *world* ,group1 = world
#                    pattern replaced by repl_expression :'<em>(group1)</em>'



###############################################################
# avoid too greedy:
"""they will match the most case if there are:"""
pattern = r'\*(.+)\*' # match anything between **
print re.sub(pattern,r'<em>\1</em>','*This* is *it*!')
# NG:it matches the first * to the end * 
# solution : add a '?'
pattern = r'\*(.+?)\*' # match anything between **
print re.sub(pattern,r'<em>\1</em>','*This* is *it*!')
# +? will try match 1 or more, but every time try minimum match
