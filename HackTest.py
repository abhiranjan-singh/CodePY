def fizzBuzz(n):


# Write your code here
 for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue

    elif i % 3 == 0 and i % 5 != 0:
        print('Fizz')
        continue
    elif i % 5 == 0 and i % 3 != 0:
        print('Buzz')
        continue
    print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)