import re

f  = open("./Challenge4equality.html", "r")

result = ""

for line in f.readlines():
	lineResultList = re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", line)
	if(len(lineResultList) != 0):
		result +=  "".join(lineResultList)

print result
f.close()
