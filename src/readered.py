from reader import *
from table import *
from sys import argv
from xval import *

csvfile = open('../data/weather1.csv','r')
readCsv(csvfile,argv[1]) #takes predicted value as arguement
print data[argv[1]]
xvals(data,2,3,'zeror',argv[1])
                                 
#tableprint(argv[1])

