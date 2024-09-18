import os

# open a pipe to the output of the ls  command
p = os.popen("ls -l")
# discard the first summary line of ls  if it causes problems
p.readline()
found = False

for line in p:
    #print(line.rstrip()) # split each line of ls  output into fields
    fields = line.split() # print each field
    name = fields[8]
    size = int(fields[4])
    
    if size > 1000:
    	found = True
    	print("Field: ",name, ", Size: ", size )
    
if found == False:
	print("There are no files found over the threshold")
   
    #i=0
    #while i < len(fields) :
    #    print("Field", i, "is", fields[i])
    #    i +=1
	
	
	
	
	
	
