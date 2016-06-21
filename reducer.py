#!/usr/bin/python

import sys
import re

prev=None
cur=None
len=0
for line in sys.stdin:
	data=line.strip().split("\t")
	cur=data[0]
	if prev == None:
		len=len+1
		prev=cur
		continue
	if cur==prev:
		len=len+1
		prev=cur
		continue
	else:
		len=1
		print prev,"\t",len
		prev=cur
print cur,"\t",len
							
