from globfile import *
from lib import *
def tableprint(csvfile): #prints table with the summary
    print rowprint(colname),'%10s' % 'notes'
    print rowprint(expected(colname)), '%10s' % 'expected'
    temp = [ c for c in colname ]
    for c in colname:
        if c in nump:
            temp[colname.index(c)] = str('%0.2f' % round(sd[c],2))
        else:
            temp[colname.index(c)] = str('%0.2f' % round(float(most[c])/float(n[c]),2))
    print rowprint(temp),'%10s' % 'certainity'
    for row in data:
        print rowprint(row)

def klass1(row, data):
    for k in klass:
        return order[k]
