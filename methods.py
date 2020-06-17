a="He found it boring and he left"
loc=a.find("boring")
a=a[:loc]+"fun"   #it removes boring and add fub to it
print(a)
b='and'.join(["cars ","  motorcycles ","  trucks "])
print(b)
c=b.split()
print(c)
d=b.split("and")
print(d)
x ="Jai Hind"
loc=x.find("Hind")
print(x)
y=x[:loc]+"Bharat"
print(y)