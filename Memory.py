#!/usr/bin/python
import os
msize = os.popen("df -h")
y=msize.read()
print(y)
