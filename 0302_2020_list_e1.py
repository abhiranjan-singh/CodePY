x=[1,3,5,7,11]
print(x)
print("x[2]=",x[2])
x[2] =0
print("Replace 5 with 0, x=",x)
x.append(13)
print ("After append, x=", x)
x.remove(1) #removes the 1, not the iteam at the postion 1!!
print("After remove item 1, x=",x)
x.insert(1,42)
print("Insert 42 at item 1=",x)



