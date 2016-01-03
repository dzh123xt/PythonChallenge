#Challenge2
import re

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

strList = list(s)

s = ""

for c in strList:
	if(ord(c) <= ord('z') and ord(c) >= ord('a')):
		if(ord(c) <= ord('z') - 2):
			c = chr(ord(c) + 2)
		else:
			c = chr((ord('a')) + (ord(c) + 2)%ord('z') - 1) 
		s += c
	else:
		s += c

print s

