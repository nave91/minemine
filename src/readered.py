from reader import *
from table import *
from sys import argv
from xval import *

csvfile = open('../data/diabetes.csv','r')
readCsv(csvfile,argv[1]) #takes predicted value as arguement
xvals(data,5,5,'zeror',argv[1],1,2)
                                 
#tableprint(argv[1])

