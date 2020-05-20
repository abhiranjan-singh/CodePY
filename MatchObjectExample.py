import re
line ="Now we are upgrading the PSI3 program"
matchstr =re.search("PSI3",line)
print("Match Starts at charector",matchstr.start())
print("Match end at charector",matchstr.end())
print("before Match",line[0:matchstr.start()])
print("After Match.",line[matchstr.end():])
