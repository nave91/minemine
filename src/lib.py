import re
from globfile import *

def line(csvfile):
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

def rowprint(row):
    columns = [ "%15s" % cell for cell in row]
    columns.append("%4s" % '#')
    return ' '.join(columns)
   
def expected(row):
    out = [c for c in colname]
    for c in row:
        if c in wordp:
            out[colname.index(c)] = str(mode[c])
        else:
            out[colname.index(c)] = str('%0.2f' % round(mu[c],2))
    return out
