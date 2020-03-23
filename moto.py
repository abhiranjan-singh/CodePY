#!/data/data/com.termux/files/usr/bin/python
import os
x = os.popen('whoami')
y = x.read()
print(y)
