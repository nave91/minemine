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
    print 'col: ',col

def makeTable(str,csvindex,tabindex):
    print 'In makeTable'
    for csvcol in str:
        csvindex+=1
        ignorere = re.compile('\?.*$')
        ignore = ignorere.match(csvcol)
        if ignore:
            continue
        else:
            tabindex+=1
            col.append([csvcol,csvindex,tabindex])
            print csvcol
            klassre = re.compile('=.*$')
            morere = re.compile('\+.*$')
            lessre = re.compile('-.*$')
            numre = re.compile('\$.*$')
            klasschk = klassre.match(csvcol)
            morechk = morere.match(csvcol)
            lesschk = lessre.match(csvcol)
            numchk = numre.match(csvcol)
            if klasschk:
                dep.append([csvcol,tabindex])
                klass.append([csvcol,tabindex])
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
        check()
    
def addRow(str):
    r = len(str)+1
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
                addRow(str)
            else:
                seen = True
                makeTable(str,csvindex,tabindex)
            


k = readCsv(csvfile)
