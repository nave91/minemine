from lib import *
import re
def makeTable(str,index):
    print 'In makeTable'
    for csvcol in str:
        index+=1
        ignorere = re.compile('\?.*$')
        ignore = ignorere.match(csvcol)
        if ignore:
            continue
        else:
            print csvcol
    #print str
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
                makeTable(str,index)
            


k = readCsv(csvfile)
