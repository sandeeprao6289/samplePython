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

def convertingTwoListsToDict():
	l1 = [i for i in xrange(1,27)]
	l2 = list(string.ascii_lowercase)
	d1 = dict(zip(l1,l2))
	print d1

def convertingTupleToDict():
	l1 = tuple([(i,i*i) for i in range(10)])
	print l1 #op ((0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81))
	print dict(l1) #op {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
	l2 = [('stud1', 4558), ('stud2', 4875), ('stud3', 5016)]
	print dict(l2) #op {'stud3': 5016, 'stud2': 4875, 'stud1': 4558}

def printKeyValue():
	d1 = {x:x*x for x in range(0,20,2) }
	print d1 
	for key,value in d1.iteritems():
		print key,value
	print d1.keys() #op [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
	print d1.values() #op [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

def testDuplicateKeys():
	d1 = {'k1':100,'k2':1000,'k1':200}
	print d1 #op {'k2': 1000, 'k1': 200}


def checkList():
	l1 = ['a','b','c','d','e','f']
	l2 = ['d','e','f','g','h','i']

	d1 = {'used':[i for i in l1 if i in l2],'unused':[i for i in l1 if i not in l2]}
	print d1

checkList()

def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value
    