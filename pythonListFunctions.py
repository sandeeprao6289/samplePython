#!/bin/bash/python

def listOfEvenNums():
	l1 = [i for i in range(100,2000,2)]
	print l1

def mergeTwoLists():
	l1 = [i for i in range(1,10)]
	l2 = [i for i in range(1,20,2)]
	l3 = l1 + l2
	l4 = list(set(l1 + l2)) #removing of duplicate elements

	print l3

def multiplyLists():
	l1 = []
	l2 = [[1]*3] #here the elements of the list are getting multiplied.
	l3 = [[1]]*3 #here the list inside the list is getting multiplied. 
	
	print l2 # op: [[1, 1, 1]]
	print l3 # op: [[1], [1], [1]]

def accessListInList():
	l1 = [[i for i in range(1,10)],[i for i in range(10,50)]]

	print l1[0]
	print l1[0][1:4]
	print l1[1][10:20]
	l1[1][10] = 56
	print l1[1][10:20]

def addingTupleInList():
	l1 = [(i,i) for i in range(10)]

	print l1[0]
	l1[0] = 1 #the tuple is replaced by integer
	print l1[1][0]
	l1[1][0] = 2 #throws error as tuple is an immutable datastructure.The immutable property of tuple holds good even is its in a list. 

def accessListInTuple():
	t1 = tuple([[i for i in range(1,10)],[i for i in range(10,20)]])

	print t1
	print t1[0]
	#t1[0] = 10 #throws error as tuple is immutable
	t1[0][2] = 45
	print t1[0] #No matter the list is inside a tuple the mutable property of list holds good.

def createDictInList():
	d1 = [{x:y} for x in range(1,10) for y in range(1,20)]#This will create x*y number of dictionaries inside the list with x as key and y as value.
	d2 = [{x:x*x} for x in range(1,10)]#This creates x number of dictionaries with x as key and x*x as value.

	print d1[0].keys() #To get the list of keys in the dict
	print d1[0].values() #To get the list of values in the dict

def createFibonacci(n):
	l1 = [fib(x) for x in range(n)]

	print l1

def fib(n):
	return n if n<=1 else (fib(n-1) + fib(n-2))

#createFibonacci(20)#op:[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

def convertLargeStringToList():
	s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."
	l1 = s1.strip(',').split(' ') #split breaks the string by converting the above string to smaller strings and inserting them to the list. Strip removes the character mentined in the method.

	l2 = [len(w) for w in l1]#get the length of each word.

	d1 = {w:len(w) for w in l1}#dictionary which contains the word as key and length as its value.
	
	print l1 #op: ['Python', 'is', 'a', 'powerful', 'high-level,', 'object-oriented', 'programming', 'language', 'created', 'by', 'Guido', 'van', 'Rossum.']
	print l2 #op: [6, 2, 1, 8, 11, 15, 11, 8, 7, 2, 5, 3, 7]
	print d1 #op: {'a': 1, 'van': 3, 'language': 8, 'created': 7, 'Python': 6, 'programming': 11, 'is': 2, 'powerful': 8, 'object-oriented': 15, 'high-level,': 11, 'Guido': 5, 'by': 2, 'Rossum.': 7}

def checkPalindrome():
	s1 = "Python is a powerful high-level, object-oriented programming language created by Guido van Rossum."

	p1 = [w for w in s1.replace(',','').strip('.').split(' ') if pal(w.lower()) and len(w)>1]

	print pal('hello') #op: False
	print pal('rotor') #op: True
	print p1 #op: ['abcba']

def pal(str):
	for i in range(0,(len(str)/2)):
		if str[i] != str[len(str)-i-1]:return False
	return True

#checkPalindrome()
'''
def pal(text):
	rev = ""
	final = "" 
	for a in range(0, len(text)):
		rev = text[len(text) - a - 1]
		final = final + rev
		return 'true' if final.lower() == text.lower() else 'false'
'''
import copy
def copyList():
	l1  = [1,10,[x for x in range(10)],[y for y in range(10,20,2)]]
	l2 = copy.copy(l1)
	l3 = copy.deepcopy(l1)

	print l1 #op [1, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 12, 14, 16, 18]]
	
	l1[1] = 20 
	l1[3][4] = 25

	#Changed the element in list l1 in 2 places.
	print l1 #op [1, 20, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 12, 14, 16, 25]]
	'''Since list l2 is a shallow copy the change in l1[1] didnt affect but the change in the list inside 
	the list relected in l2 as it was just a reference object.'''
	print l2 #op [1, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 12, 14, 16, 25]]
	'''Since list l3 was a deep copy the changes in l1 wont affect as its created a cmplete copy of the 
	list object including the compound objects inside the list'''
	print l3 #op [1, 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 12, 14, 16, 18]]

copyList()