#Usage python readered.py "<data set name>"

from reader import *
from table import *
from sys import argv
from xval import *
from uxval import *

csvfile = open('../data/'+argv[1]+'.csv','r')
z ="both" # or argv[2]
a = "" # or "--once" or argv[3]
readCsv(csvfile,z) #takes predicted value as arguement
print argv[1]
print "zeror"
xvals(data,5,5,'zeror',z,2,1)
print ""
print "nb"
xvals(data,5,5,'nb',z,2,1)
print ""
print "knn"
uxvals(data,5,5,'knasd',z,2,1,a)
                                 
#tableprint(z)

