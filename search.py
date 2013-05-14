#!/usr/bin/env python

# Exctract routine signatures from a C++ module
import re

def loadtxt(filename):
    "Load text file into a string. I let FILE exceptions to pass."
    f = open(filename)
    txt = ''.join(f.readlines())
    f.close()
    return txt

# regex group1, name group2, arguments group3
rproc = r"((?<=[\s:~])(\w+)\s*\(([\w\s,<>\[\].=&':/*]*?)\)\s*(const)?\s*(?={))"
#code = loadtxt('test.c')
f=open('test.c')
cppwords = ['if', 'while', 'do', 'for', 'switch']
for c in f.readlines():
	print c,
	match   = re.finditer(rproc,c)
	#print match
	for i in match:
		name = i.group(2)
	#	print i
		arg = i.group(3)
		if name not in cppwords:
			print '\t_LOG("'+ name + '","' + arg + '");',

