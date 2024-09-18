# Q2
#import os
#import glob
#found = False
#
#for filename in glob.glob('*'):
#	if os.path.getsize(filename) > 2000:
#		found = True
#		print("File name", filename, "has size", str(os.path.getsize(filename)), "bytes")
#        # the filesize function returns the size in bytes
#if found == False:
#	print("There are no files found over the threshold")

import os
import glob
import sys
try:
	size = sys.argv[1]
	if int(size) < 1:
		print("Not correct input")
		sys.exit(0)
	else:
		found = False
		for filename in glob.glob('*'):
			if os.path.getsize(filename) > int(size):
				found = True
				print("File name", filename, "has size", str(os.path.getsize(filename)), "bytes")
	  	      # the filesize function returns the size in bytes
		if found == False:
			print("There are no files found over the threshold")

except:
	print("Not correct input")
	sys.exit(0)
	
	

