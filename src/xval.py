#! /bin/python
import lib
import reader

def xvals(csvfile,x,b,f,a):
    rows = indexes(csvfile)
    s = int(len(rows)/b)
    while x>0:
        shuffle(rows)
        for b1 in range(0,b):
            xval(b1*s+1, (b1+1)*s, rows, csvfile, f, a)

def  xval(start, stop, rows, csvfile, f, a):
    rmax = len(rows)
    test = []*(end - start)
    for i in range(1, rmax+1):
        d = rows[r]
        if r >= start && r <= end:
            test[r] = d
        else:
            temp = klass1(d, data)
            hypotheses[temp] += 1
            if hypotheses[temp] == 1:
                makeTable(
