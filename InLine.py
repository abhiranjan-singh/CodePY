import re
infile =open("E:/test.txt",'r')
lines=infile.readlines()
infile.close()

mactstr=re.compile("Abhiranjan",re.IGNORECASE)
for line in lines:
    line=mactstr.sub('RAM',line)
print(line)