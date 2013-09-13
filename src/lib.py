import re
from globfile import *

def line(csvfile): #returns formatted line from the csvfile 
    l = csvfile.readline()
    endcommare = re.compile('.*,$')
    if l != '':
        l = l.split('#')[0]
        l = l.replace('\t','')
        l = l.replace('\n','')
        l = l.replace(' ','')
        endcomma = endcommare.match(l)
        if endcomma:
            return l+line(csvfile)
        else:
            return l
    else:
        return -1

def rowprint(row): #returns neat rows
    columns = [ "%15s" % cell for cell in row]
    columns.append("%4s" % '#')
    return ' '.join(columns)
   
def expected(row): #returns expected outcome
    out = [c for c in colname]
    for c in row:
        if c in wordp:
            out[colname.index(c)] = str(mode[c])
        else:
            out[colname.index(c)] = str('%0.2f' % round(mu[c],2))
    return out

def indexes(lst):
    out = []*len(lst)
    for i in lst:
        out[i] = i
    return out
