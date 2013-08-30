import re
csvfile = open('../data/weather1.csv','r')
csvindex = -1
tabindex = -1
col = []
klass = []
more = []
less = []
num = []
term = []
dep = []
indep = []
nump = []
wordp = []
hi = []
lo = []
mu = []
m2 = []
sd = []
count = []
mode = []
most = [] 
isnum = True
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

