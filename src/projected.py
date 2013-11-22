from project import *
from reader import *
def projected():
    projected1("data/automsg.csv")

def projected1(f):
    readCsv(f,0)
    w = project(0,data)
    tableprint(0)

projected()
