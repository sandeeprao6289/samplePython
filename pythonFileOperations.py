import csv

def readCSVFile():
	csvfile = open('states.csv','rw')
	rows = csv.DictReader(csvfile)

	states = [(row['STATE'],row['CODE']) for row in rows]

	states = tuple(states)
	print states

	for state in states:print state[0],"++++",state[1]

#readCSVFile()

def readWriteCSVFile():
	csvfile = open('states.csv','rw')
	rows = csv.DictReader(csvfile)

	ofile  = open('test.csv', "wb")
	writer = csv.writer(ofile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['STATES','CODE']) 
	for row in rows:writer.writerow([row['STATE'],row['CODE']])

#readWriteCSVFile()

import xml.etree.ElementTree as ET
def readingXMLFile():
	tree = ET.parse('sample.xml')
	root = tree.getroot()


readingXMLFile()