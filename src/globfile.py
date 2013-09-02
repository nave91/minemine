#Info for table
#
csvindex = -1 #initialized to -1 as lists start at zero
colname = [] #stores names of columns
data = [] #stores list of lists containing each row
#
#metadata
#
order = dict.fromkeys(colname) #stores colnames and index of column in csv
klass = [] #list of klass columns
more = [] #list of more columns
less = [] #list of less columns
num = [] #list of num columns
term = [] #list of term columns
dep = [] #list of dependent columns
indep = [] #list of independent columns
nump = [] #list containing nump column names
wordp = [] #list containing wordp column names
#
#for nump values
#
hi = dict.fromkeys(nump) #dictionary containing highest values of nump columns 
lo = dict.fromkeys(nump) #dictionary containing lowest values of nump columns
mu = dict.fromkeys(nump) #dictionary containing mean values of nump columns
m2 = dict.fromkeys(nump) #dictionary containing m2 values of nump columns
sd = dict.fromkeys(nump) #dictionary containing std dev of nump columns
#
#for wordp values
#
mode = dict.fromkeys(wordp) #dictionary containing mode of wordp columns
most = dict.fromkeys(wordp) #dictionary containing most occured item of wordp columns
count = dict((dict.fromkeys(wordp))) #dictionary of dictionaries of count of each item in each wordp column
#
#for all
#
n = dict.fromkeys(colname) #stores number of elements in each column
isnum = True
