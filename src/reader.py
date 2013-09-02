import re
from lib import *

def check():
    print "\n\n"
    print 'dep: ',dep
    print 'indep: ',indep
    print 'klass: ',klass
    print 'more: ',more
    print 'less: ',less
    print 'num: ',num
    print 'term: ',term
    print 'nump: ',nump
    print 'colname: ',colname
    print 'order: ',order
    print 'data: ',data
    print 'hi: ',hi
    print 'lo: ',lo
    print 'mu: ',mu
    print 'sd: ',sd
    print 'wordp: ',wordp
    print 'count: ',count
    print 'mode: ',mode
    print 'most: ',most

def makeTable(str,csvindex):
    for csvcol in str:
        isnum=True
        csvindex+=1
        ignore = re.match('\?.*$',csvcol)
        if ignore:
            continue
        else:
            colname.append(csvcol)
            order[csvcol] = csvindex
            klasschk = re.match('=.*$',csvcol)
            morechk = re.match('\+.*$',csvcol)
            lesschk = re.match('-.*$',csvcol)
            numchk = re.match('\$.*$',csvcol)
            if klasschk:
                dep.append(csvcol)
                klass.append(csvcol)
                isnum = False
            elif morechk:
                dep.append(csvcol)
                more.append(csvcol)
            elif lesschk:
                dep.append(csvcol)
                less.append(csvcol)
            elif numchk:
                indep.append(csvcol)
                num.append(csvcol)
            else:
                indep.append(csvcol)
                term.append(csvcol)
                isnum = False
            n[csvcol] = 0
            if isnum:
                nump.append(csvcol)
                hi[csvcol] = 0.1 * (-10**13)
                lo[csvcol] = 0.1 * (10**13)
                mu[csvcol] = 0.0
                m2[csvcol] = 0.0
                sd[csvcol] = 0.0
            else:
                wordp.append(csvcol)
                count[csvcol] = dict()
                mode[csvcol] = 0
                most[csvcol] = 0
                
    
def addRow(str,predclass,pred,colname,data,csvindex):
    temp = []
    skip = False
    if predclass in klass:
        csvindex = order[predclass]
        item = str[csvindex]
        if item == pred:
            skip = False
        elif pred == 'both':
            skip = False
        else:
            skip = True
    else:
        print 'WARNING: Class to be predicted is not in klass'
    if skip:
        return
    for c in colname:
        csvindex = order[c]
        item = str[csvindex]
        uncertain = re.match('\?',item)
        if uncertain:
            temp.append(item)
        else:
            n[c] += 1
            if c in wordp:
                temp.append(item)
                try:
                    new = count[c][item] = count[c][item] + 1
                    if new > most[c]:
                        most[c] = new
                        mode[c] = item
                except KeyError:
                    count[c][item] = 1
                    if count[c][item] > most[c]: 
                        most[c] = 1
                        mode[c] = item
            else:
                item = float(item)
                temp.append(item)
                if item > hi[c]:
                    hi[c] = item
                if item < lo[c]:
                    lo[c] = item
                delta = item - mu[c]
                mu[c] += delta / n[c]
                m2[c] = delta * (item - mu[c])
                if n[c] > 1:
                    sd[c] = (m2[c] / (n[c] - 1)**0.5)
    data.append(temp)    

def readCsv(csvfile,predclass,pred):
    seen = False
    FS = ','
    while True:
        str = line(csvfile)
        if str == -1:
            print 'WARNING: empty or missing file'
            return -1 
        str = str.split(FS)
        if str != ['']:
            if seen:
                addRow(str,predclass,pred,colname,data,csvindex)
            else:
                seen = True
                makeTable(str,csvindex)
#csvfile = open('../data/weather1.csv','r')
#readCsv(csvfile,'=play','no')
#check()
