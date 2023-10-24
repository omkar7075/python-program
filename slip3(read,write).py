#slipno3
#read write file
f1=open('first.txt',r) 
f2=open('second.txt',w) 
line=f1.readline()
f2.write(line)
f1.close()
f2.close()
