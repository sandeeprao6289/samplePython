def createDictUsingDictComprehensions():
	d1 = {x:x*2 for x in range(10)}
	d2 = {x:x*x for x in range(10)}
	print d1 #op {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

def createDict():
	d1 = {'a':1,'b':2}
	d1['c'] = 3
	d1['l'] = [x for x in range(10,20)]

	print d1 #op {'a': 1, 'c': 3, 'b': 2, 'l': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]}

import string

def dictComprehensions():
	l1 = [i for i in xrange(1,27)]
	l2 = list(string.ascii_lowercase)
	d1 = dict(zip(l1,l2))
	print d1
	d2 = {x+1:y for x,y in enumerate(l2) }
	print d2
	for i,j in d2.iteritems():
		print "+++++++",i,"+++++++",j,"+++++++"

def convertingTupleToDict():
	l1 = tuple([(i,i*i) for i in range(10)])
	print l1
	print dict(l1)

convertingTupleToDict()
