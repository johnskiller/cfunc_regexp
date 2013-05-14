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
rproc = r"((?<=[\s:~])(\w+)\s*\(([\w\s,<>\[\].=&':/*]*?)\)\s*(const)?\s*({))"
cppwords = ['if', 'while', 'do', 'for', 'switch']
#code = loadtxt('test.c')

def func_replace(matchobj):
	return matchobj.string+'\n'+'\t_LOG('+matchobj.group(2)+'('+matchobj.group(3)+');'

def proc_sub():
	code = loadtxt('test.c')
	print re.sub(rproc,func_replace,code)

def proc_stream():
	code = loadtxt('test.c')
	procs = [ [i,i.group(2), i.group(3)] for i in re.finditer(rproc, code) \
 		if i.group(2) not in cppwords]

	for i in procs: print '***['+i[0].string+']***',i[1] + '(' + i[2] + ')'

def proc_line():
    f=open('test.c')
    for c in f.readlines():
        print c,
        match   = re.finditer(rproc,c)
        #print match
        for i in match:
            name = i.group(2)
        #    print i
            arg = i.group(3)
            if name not in cppwords:
                print '\t_LOG("'+ name + '","' + arg + '");',

def proc_search():
	code = loadtxt('test.c')
	ro = re.compile(rproc)
	pos = 0;
	m=ro.search(code,pos)
	while m:
		print code[pos:m.end()]
		if m.group(2) not in cppwords:
			print '\t_LOG(',m.start(),',',m.end(),', "func='+m.group(2)+'('+m.group(3)+')" );'
		pos=m.end()
		m=ro.search(code,pos)

	#output rest
	print code[pos:]
if __name__ == '__main__':
    proc_search()