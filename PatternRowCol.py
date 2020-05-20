for row in range (1,5):
    for col in range(1,9):
        if (row==1 and col==4 or row==2 and col in range(3,6) or row==3 and col in range(2,7) or row==4 and col in range(1,8) or row==5 and col in range(0,9) ):
            print("*",end="")
        else:
            print("+",end="")
    print()