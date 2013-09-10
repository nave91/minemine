from reader import *
from table import *
from sys import argv
csvfile = open('../data/weather1.csv','r')
readCsv(csvfile,argv[1],argv[2]) #takes predicted column as 
                                 #first arguement and predicted value as second arguement
                                 
tableprint(csvfile)

