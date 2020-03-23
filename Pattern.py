for row in range (0,5):
    for col in range (0,5):
        if (col==2 and row == 0 or col in range(1,4) and row == 1 or col in range (0,5) and row== 2  ):
            print('*',end="")
        else:
            print(' ',end="")
    print()