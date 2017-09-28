from collections import namedtuple,defaultdict

def testNamedTuple():
	Animal = namedtuple('Animal', 'name age type')
	perry = Animal(name="perry", age=31, type="cat")

	print(perry)
	# Output: Animal(name='perry', age=31, type='cat')

	#perry.name = "lol"
	perry = perry._replace(name=33)

	print(perry.name)
	# Output: 'perry' 

def testDefaultDict():
	d1 = {'A':1,'B':2,'C':3,'D':1}

	d = defaultdict(list)

	for k,v in d1.iteritems():
		d[v].append(k)

	print dict(d)

#testDefaultDict()

def testDictFunction():
	d1 = {'A':1,'B':2,'C':3,'D':1}
	d2 = {}
	for item in d1.keys():
		if d2.has_key(d1[item]):
			d2[d1[item]] = [d2[d1[item]]] + [item]
		else:
			d2[d1[item]] = item

	print d2

#testDictFunction()
