import sys
import string

fileinput = sys.argv[1]
fileoutput = sys.argv[2]

f = open(fileinput, 'r')
outputfile = open(fileoutput, 'wb')
finalstring = ""
randomstring = ""
for line in f:
	randomstring = line.replace(" ", "")
	randomstring = randomstring.rstrip("\r\n")
	if(len(randomstring) % 2):
		randomstring = randomstring[0:len(randomstring)-1]
	finalstring += randomstring
#randomstring = randomstring.decode("hex")
print len(finalstring)
finalstring = finalstring.decode("hex")
outputfile.write(finalstring)
f.close()
outputfile.close
	
