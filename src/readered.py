from reader import *
from table import *
from sys import argv
from xval import *
from uxval import *

csvfile = open('../data/'+argv[1]+'.csv','r')
readCsv(csvfile,argv[2]) #takes predicted value as arguement
a = argv[3]
print argv[1]
print "zeror"
xvals(data,5,5,'zeror',argv[2],2,1)
print ""
print "nb"
xvals(data,5,5,'nb',argv[2],2,1)
#print "knn"
#uxvals(data,5,5,'knasd',argv[2],2,1,a)
                                 
#tableprint(argv[1])

