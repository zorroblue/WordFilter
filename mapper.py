#!/usr/bin/python
import sys
import re


for line in sys.stdin:
	data=line.strip().split(" ") #the web logs are tab delimited
	#print data
	if(len(data)!=10):
		continue
	else:
		if data[6].find("dummy")!=-1: #For now , let "dummy" be the dummy word
			print data[0],"\t",data[6]
			
