def f1(x,y):
    x=x*1
    y=y*2
   # return (x,y)
    print (x,y)
def f2(x,y):
    x=x*1
    y[0]=y[0]*2
    print (x,y)
a=0
b=[1,2]
f1(a,b)
print (a,b)
f2(a,b)
print(a,b)