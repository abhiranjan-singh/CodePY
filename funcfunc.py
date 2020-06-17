def iseven(x,f):
    if (f(x) == f(-x)):
        return True
    else:
        return False
def square(n):
    return(n*n)
def cube(n):
    return(n*n*n)
print (iseven(2,square))
print (iseven(2,cube))