"""Q31.Write a program to print out all Armstrong numbers between 1 and 500.
If the sum of cubes of each digit of the number is equal to the number itself,
then the number is called an Armstrong number."""

for i in range(1, 501):
    power = len(str(i))
    x = i
    sum = 0
    while x > 0:
        digit = x % 10
        sum += digit ** power
        x //= 10
    if i == sum:
        print(i)

"""Output:-
1
2
3
4
5
6
7
8
9
153
370
371
407
"""
