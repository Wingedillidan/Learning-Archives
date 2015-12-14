# beginner save/loading =D

from sys import argv
from os.path import exists

scriptname, filename = argv

file = open(filename)
contents = file.read()
filew = open(filename, 'w')

print """
This file's contents:
--------------\n
%s
\n--------------""" % contents

add = raw_input('What to add? ')

filew.write("%s\n%s" % (contents, add))

print """
This file's NEW contents:
--------------\n
%s
\n--------------""" % "%s\n%s" % (contents, add)

print "Saving..."
file.close()
filew.close()
print "Done!"