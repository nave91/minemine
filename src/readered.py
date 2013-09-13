from reader import *
from table import *
from sys import argv
from xval import *

csvfile = open('../data/soybean.csv','r')
readCsv(csvfile,argv[1]) #takes predicted value as arguement
xvals(data,2,2,'zeror',argv[1])
                                 
#tableprint(argv[1])

