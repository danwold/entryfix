import csv
import sys
import re


entrylist = []
tails = []

try:

	filename = sys.argv[1]

except IndexError:

	print "No Input File"
	sys.exit()

try:

	with open('tails','rb') as csvfile:
		for row in csv.reader(csvfile,delimiter=','):
			tails.append(row)

	with open(filename,'rb') as csvfile:
		for row in csv.reader(csvfile,delimiter=','):
			entrylist.append(row)

except IOError:

	print "File Open Error"
	sys.exit()

entrylist[0].append('nid')

for entry in entrylist[1:]:
	entry[10] = re.sub('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][" "]','',entry[10])
	entry[11] = re.sub('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][" "]','',entry[11])
	entry[12] = re.sub('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][" "]','',entry[12])

	entry[2] = 'E145'

	entry[3] = entry[3].strip()

	for tail in tails:
		if entry[3] == tail[1]:
			 entry.append(tail[0])

try:
	with open(sys.argv[2],'w') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')
		for row in entrylist:
			writer.writerow(row)
		print "File "+sys.argv[2]+" Created"

except IOError:
	print "File Write Error"
	
except IndexError:
	
	try:

		with open(filename,'w') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')
			for row in entrylist:
				writer.writerow(row)

	except IOError:
		print "File Write Error"


