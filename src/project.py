def project(t,data):
    d  = anyi(data)
    x = []
    y = []
    east = furthest(d,data,t)
    west = furthest(d,data,t)
    project0(east,west,data,t,x,y)
    return widen(t,x,y)

def project0(east,west,data,t,x,y):
    print "+"
    bigger = 1.05
    some = 0.000001
    inde = data[z].index(east)
    indw = data[z].index(west)
    c = dist(data[z][inde],data[z][indw],data,z,indep,nump)
    for d in data:
        ind = data.index(d)
        a = dist(data[ind],data[east])
        b = dist(data[ind],data[west])
        if b > c*bigger:
            return project0(east,d,data,t,x,y)
        if a > c*bigger:
            return project0(d,west,data,t,x,y)
        print "."
        x[d] = (a^2 + c^2 - b^2) / (2*c + some)
        y[d] = (a^2 - x[d]^2)^0.5

def widen(t,x,y):
    adds = colname[t]
    adds.extend("$_XX")
    adds.extend("$_yy")
    adds.extend("$_Hell")
    adds.extend("_ZZ")
    w = "__"+t
    makeTable(adds,w)
    for d in data[t]:
        ind = data[t].index(d)
        hell = fromHell(data[t][ind],t)
        wider = data[t][ind]
        wider.extend(x[d])
        wider.extend(y[d])
        wider.extend(hell)
        wider.extend(0)
        addRow(wider,w)
    return w

    
        
