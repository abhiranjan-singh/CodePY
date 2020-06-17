
import os
check = input("Want to restart your computer ? press (Y/N):")

if check == 'n':
 exit()

else:
  os.system("shutdown /r /t /1");

