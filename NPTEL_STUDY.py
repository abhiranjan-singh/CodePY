import os
pi = 3.14
print (pi)
print ("2*2=",2**2)
x = 1
print (type(x),type(pi))

user = os.getlogin()
admin = 'a.singh'
if admin == user:
    print ("user has all privileges",user)
else:
    print("user does not have all privileges",user)

print (os.curdir)
print (os.getcwd())
print(globals