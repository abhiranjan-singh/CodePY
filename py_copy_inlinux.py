
#!/data/data/com.termux/files/usr/bin/python
import os
mk_dir= os.popen('mkdir  /data/data/com.termux/files/home/test/`date +%d_%b__%m`')
R_mk_dir=mk_dir.read()
copy=os.popen('cp -r /data/data/com.termux/files/home/27_02_20/* /data/data/com.termux/files/home/test/`date +%d_%b__%m`')
r_copy=copy.read()

