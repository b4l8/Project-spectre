#! /usr/bin/env python

# urllib or urllib2 :
#                   urllib2 better
#                   simple download: urllib
#                   need HTTP authentication, cookie,protocole,extenstion program : urllib2

from urllib import urlopen
from urllib import urlretrieve
import re
# open distance file
webpage = urlopen('http://www.python.org')
text = webpage.read()

m = re.search('<a href="([^"]+)" .*?>about</a>',text,re.IGNORECASE)

print m.group(1)

# download distance file

urlretrieve('http://www.python.org','python_webpage.html')
