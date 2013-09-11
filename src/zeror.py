from reader import *
from  xval import *
from lib import *

def zeror(test,data,hypotheses,z):
    hmost = -10**23
    acc = 0
    for h in hypotheses:
        these = len(data[h])
        if these > hmost:
            most = these
            got = h
    print "#got: ",got
    where = klassAt(z)
    for t in test:
        want = t[where]
        if want == got:
            acc+=1.0
    print 100*acc/len(test),"\t"
