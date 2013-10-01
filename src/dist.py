#! /usr/bin/env python
from reader import *

def dist(this,that,data,z,indep,nump):
    tot = 0.0
    for k in indep:
        ind = colname[z].index(k)
        v1 = this[ind]
        v2 = that[ind]
        if v1 == "?" and v2 == "?":
            tot+=1
        elif k in nump:
            aLittle = 0.0000001
            if v1 == "?":
                v1 = 1 if v2 < 0.5 else 0
            else:
                v1 = (v1 - lo[z][k])/ (hi[z][k] - lo[z][k] + aLittle)
            if v2 == "?":
                v2 = 1 if v1 < 0.5 else 0
            else:
                v2 = (v2 - lo[z][k])/ (hi[z][k] - lo[z][k] + aLittle)
            tot += (v2-v1)**2
        else:
            if v1 == "?":
                tot += 1
            elif v2 == "?":
                tot += 1
            elif v1 != v2:
                tot += 1
            else:
                tot += 0
    ret = tot**0.5 / (len(indep))**0.5
    return ret