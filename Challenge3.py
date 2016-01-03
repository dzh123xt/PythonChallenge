import re

f  = open("./Challenge3ocr.html", "r")

result = ""

for line in f.readlines():
	content =  re.sub("([^a-zA-Z]*)", "", line)
	if(content != ""):
		print content,
print result 
f.close()
