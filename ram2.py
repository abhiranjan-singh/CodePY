import subprocess
result = []
win_cmd = 'ipconfig'(h.shandilya,ram2.py,'10.199.165.35')
process = subprocess.Popen(win_cmd,
shell=True,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE )
for line in process.stdout:
    print (line)
result.append(line)
errcode = process.returncode
for line in result:
    print (line)