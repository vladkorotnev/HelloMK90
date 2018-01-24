#!/usr/bin/python

# Converts binary file to Octal directives of MACRO-11

import sys
strs = "; Programmatically generated from "+sys.argv[1]
strs += " - DO NOT EDIT!\r\n"

with open(sys.argv[1],'rb') as f:
	while 1:
		byte_s = f.read(1)
		if not byte_s:
			break
		strs += ".byte "
		strs += oct( ord( byte_s ) )
		strs += "\r\n"
print strs.rstrip(', ')

