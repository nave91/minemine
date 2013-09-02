from reader import *
from table import *
from sys import argv
csvfile = open('../data/weather1.csv','r')
readCsv(csvfile,argv[1],argv[2])
tableprint(csvfile)

