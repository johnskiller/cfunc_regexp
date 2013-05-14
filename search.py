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
code = loadtxt('test.c')
cppwords = ['if', 'while', 'do', 'for', 'switch']
procs = [(i.group(2), i.group(3)) for i in re.finditer(rproc, code) \
 if i.group(2) not in cppwords]

for i in procs: print i[0] + '(' + i[1] + ')'
