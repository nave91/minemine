#! /bin/python
from lib import *
from reader import *
from table import *
from zeror import *

def xvals(data,x,b,f,z):
    rows = indexes(data,z)
    s = int(len(rows)/b)
    while x>0:
        shuffled(rows)
        for b1 in range(0,b):
            xval(b1*s+1, (b1+1)*s, data, rows, f, z)
        x=x-1

def  xval(start, stop, data, rows, f, z):
    rmax = len(rows)
    test = []
    hypotheses = {}
    newddict(data,z)
    for r in range(1, rmax):
        d = rows[r]
        if r >= start and r <= stop:
            test.append(d)
        else:
            temp = klass1(d, z)
            try:
                hypotheses[temp] += 1
                if hypotheses[temp] == 1:
                    makeTable(colname[z],temp)
                addRow(d,temp)
            except KeyError:
                hypotheses[temp] = 1
                if hypotheses[temp] == 1:
                    makeTable(colname[z],temp)
    zeror(test, data, hypotheses, temp) 
    xvalTest1(test,data,hypotheses)

def xvalTest1(test,data,hypotheses):
    print "\n=================================="
    for h in hypotheses:
        tableprint(h)
