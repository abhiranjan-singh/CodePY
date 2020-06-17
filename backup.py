#!/usr/bin/python
import os
import subprocess


mk_dir = os.popen('mkdir /webserver-backup/web_bkp/`date +%d_%m_%y`')
r_mk_dir=mk_dir.read()

copy = os.popen('cp -r /usr/local/apache24/   /webserver-backup/web_bkp/`date  +%d_%m_%y`')
paste =copy.read()

