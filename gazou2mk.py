#!/usr/bin/python

from PIL import Image
import sys

im = Image.open(sys.argv[1]).point(lambda x: not bool(x))
if im.width != 120 or im.height != 64:
	print "Image is not 120x64 1bit image"
	sys.exit(-1)

pix = im.load()

# Build half-half interlaced image

outfile = ""

for y in range(0,im.height/2):
	# Encode 1 byte of top line, 1 byte of bottom line
	x = 0
	while x < im.width:
		curr_byte = 0x0
		for i in range(0,8):
			curr_byte = curr_byte << 1
			curr_byte += pix[int(x+i), y]
		outfile += chr(curr_byte)
		curr_byte = 0x0
		for i in range(0,8):
			curr_byte = curr_byte << 1
			curr_byte += pix[int(x+i), y + im.height/2]
		outfile += chr(curr_byte)
		x += 8


with open(sys.argv[1]+'.mk90', 'wb') as f:
	f.write(outfile)
	f.close()