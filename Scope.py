a = 5
globalVar ="This Is Global"

def MyFunction():
    localVar="This Is Local"
    globalVar="This Is Local"
    print("myfunction - LocalVar: "+  localVar)
    print("myfunction -globalVar: "+  globalVar)
MyFunction()
print( globalVar)

def func(b):
    c =a+b
    return (c)
print (func(4))  #gives 4+5=9
print (c)   #not defined



