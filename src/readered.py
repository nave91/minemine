from reader import *
from table import *
from sys import argv
from xval import *

csvfile = open('../data/'+argv[1]+'.csv','r')
readCsv(csvfile,argv[2]) #takes predicted value as arguement
xvals(data,5,5,'nb',argv[2],1,2)
                                 
#tableprint(argv[1])

