from lib import *
import re
from globfilerank import *

def obs(f,alli):
    now = alli
    line = f.readline()
    while(line):
        lst = line.split()
        for i in lst:
            isitnum = re.match('^([^0-9]|\.)',i)
            if isitnum:
                now = i
            else:
                v = float(i)
                inc(v,now)
                inc(v,alli)
        f.close()
        for i in name:
            if i != alli:
                order[i]["="] = i
                order[i]["x"] = mu[i]
        line = f.readline()

def inc(v,k):
    name.append(k)
    label[k] = 0
    try:
        n[k] += 1
    except KeyError:
        n[k] = 1
    alli = n[k]
    try:
        x[k][alli] = v
    except KeyError:
        x[k] = {}
        x[k][alli] = v
    try:
        sumi[k] += v
    except KeyError:
        sumi[k] = v
    delta = v - mu[k]
    try:
        mu[k] += delta/alli
    except KeyError:
        print "hello"
        mu[k] = delta/alli
    print k
    print mu[k]
    try:
        m2[k] += delta*(v - mu[k])
    except KeyError:
        m2[k] = delta*(v - mu[k])
    var[k] = m2[k]/(alli - 1 + PINCH)

def rank(alli,a,cohen,mittas,a12):
    cohen = cohen*(var[alli])**0.5
    level = 0 
    total = ns[alli]
    rdiv(0,len(order),1,cohen,mittas,a12)
    
def rdiv(low,high,c,cohen,mittas,a12):
    cut = div(low,high,cohen,mittas,a12)
    if cut:
        level += 1
        c = rdiv(low,cut-1,c) + 1
        c = rdiv(cut,high,c)
    else:
        for i in range(low,high):
            labels[order[i]["="]] = c
    return c

def div(low,high):
    muAll = divInits(low,high)
    maxi = -1
    for i in range(low,high):
        b = order[i]["="]
        n0[i] = n0[i-1] + ns[b]
        sum0[i] = sum0[i-1] + sumi[b]
        left = n0[i]
        muLeft = sum0[i] / left
        right = n1[i]
        muRight = sum0[i] / right
        e = errDiff(muAll,left,muLeft,right,muRight)
        if cohen:
            if abs(muLeft - muRight) <= cohen:
                continue
        if mittas:
            if e < maxi:
                continue
        if a12:
            if bigger(low,i,high) < a12:
                continue
        maxi = e
        cut = i
    return cut

def errDiff(mu,n0,mu0,n1,mu1):
    return n0*(mu - mu0)**2 + n1*(mu - mu1)**2

def diffInits(low,high):
    b= order[lo]["="]
    n0[lo]= n[b]
    sum0[lo]= sumi[b]
    b= order[hi]["="]
    n1[hi]= n[b]
    sum1[hi]= sumi[b]
    for i in range(hi,lo-1,-1):
        b = order[i]["="]
        n1[i] = n1[i+1] + n[b]
        sum1[i] = sum1[i+1] + sumi[b]
    return sum1[low]/n1[low]

def bigger(low,mid,high):
    below =  []
    above = []
    values(below,low,mid-1)
    values(above,mid,high)
    return a12statistic(below,above)

def a12statistic(below,above):
    for j in enumerate(above):
        for i in enumerate(below):
            comparisons += 1
            more += above[j] if above[j] > below[j] else below[i]
            same += above[j] if above[j] == below[j] else below[i]
    return (more + 0.5*same)/comparisons

def values(out,i,j):
    out = []
    m = 0
    for k in range(i,j):
        b = order[k]["="]
        for l in enumerate(x[b]):
            m += 1
            out[m] = x[b][l]
    return m

def ranks(f,cohens,mittas,a12):
    print "\n----|,",f.name,"|------------------"
    obs(f,0)
    rank(0,a,cohens,mittas,a12)
    maxi = len(order)
    for i in range(0,maxi):
        k = order[i]["="]
        print k,names[k],":mu",mu[k],":rank",labels[k]        

f = open('../data/ska.txt','r')
ranks(f,0.3,1,0.6)
