import os
string = "THIS SHOULD ALL BE LOWERCASE."[::-1]   #[::-1 it reverses each letter of the word]
print(string.swapcase())   #string.swapcase this function converts lower in to upper uppr in to lower

string = "aWESOME is cODING"[::-1]
print(string.swapcase())


def rev_sentence(sentence):
    # first split the string into words
    words = sentence.split(' ')

    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))

    # finally return the joined string
    return reverse_sentence


if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(rev_sentence(input))


    #****************************************************
    # !/bin/python

    import math
    import os
    import random
    import re
    import sys


    #
    # Complete the 'reverse_words_order_and_swap_cases' function below.
    #
    # The function is expected to return a STRING.
    # The function accepts STRING sentence as parameter.
    #

    def reverse_words_order_and_swap_cases(sentence):
        # Write your code here
        words = sentence.split(' ')
        reverse_sentence = ' '.join(reversed(words))
        x = reverse_sentence.swapcase()
        return x


    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        sentence = input()

        result = reverse_words_order_and_swap_cases(sentence)

        fptr.write(result + '\n')

        fptr.close()
