"""Q34. Write a program to find the octal equivalent of the entered number."""

num = int(input("Enter a decimal no.: "))


base = 1
octal = 0
while num > 0:
    rem = num % 8
    num = int(num / 8)
    octal = octal + (rem * base)
    base = base * 10

print("Octal equivalent of the entered number(Decimal number) is {0}.".format(octal))


"""Output:-
Enter a decimal no.: 26
Octal equivalent of the entered number(Decimal number) is 32.
"""