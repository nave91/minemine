from lib import *
import re

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
    print 'col: ',col
    print 'hi: ',hi
    print 'lo: ',lo
    print 'mu: ',mu
    print 'sd: ',sd
    print 'wordp: ',wordp
    print 'count: ',count
    print 'mode: ',mode
    print 'most: ',most

def makeTable(str,csvindex,tabindex):
    print 'In makeTable'
    for csvcol in str:
        isnum=True
        csvindex+=1
        ignore = re.match('\?.*$',csvcol)
        if ignore:
            continue
        else:
            tabindex+=1
            col.append([csvcol,csvindex,tabindex])
            print csvcol
            klasschk = re.match('=.*$',csvcol)
            morechk = re.match('\+.*$',csvcol)
            lesschk = re.match('-.*$',csvcol)
            numchk = re.match('\$.*$',csvcol)
            if klasschk:
                dep.append([csvcol,tabindex])
                klass.append([csvcol,tabindex])
                isnum = False
            elif morechk:
                dep.append([csvcol,tabindex])
                more.append([csvcol,tabindex])
            elif lesschk:
                dep.append([csvcol,tabindex])
                less.append([csvcol,tabindex])
            elif numchk:
                indep.append([csvcol,tabindex])
                num.append([csvcol,tabindex])
            else:
                indep.append([csvcol,tabindex])
                term.append([csvcol,tabindex])
                isnum = False
            if isnum:
                nump.append([csvcol,tabindex])
                hi.append([-10**13,tabindex])
                lo.append([10**13,tabindex])
                mu.append([0,tabindex])
                m2.append([0,tabindex])
                sd.append([0,tabindex])
            else:
                wordp.append([csvcol,tabindex])
                count.append([0,tabindex])
                mode.append([0,tabindex])
                most.append([0,tabindex])
    check()
    
def addRow(str,col,data,csvindex,tabindex):
    temp = []
    for i in range(0,len(col)):
        item = str[col[i][1]]
        temp.append(item)
        uncertain = re.match('\?',item)
        if uncertain:
            print 'hello'
    data.append(temp)
    print data
    #print str
def readCsv(csvfile):
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
                addRow(str,col,data,csvindex,tabindex)
            else:
                seen = True
                makeTable(str,csvindex,tabindex)
            


k = readCsv(csvfile)