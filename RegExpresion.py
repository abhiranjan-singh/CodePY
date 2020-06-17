import re
line="Upgrade the v1 programm to v2.v1 was and excellent program"


matchstr=re.split("v1",line)
for i in matchstr:
 print(i)