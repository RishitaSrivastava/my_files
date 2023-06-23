#Q15. If a five-digit number is input through the keyboard, write a program to print a new number by adding one to each of its digits.
#For example, if the number that is input is 12391 then the output should be displayed as 23402.

# Taking input
n = int(input("Enter 5 digit number: "))

# Program to print a new number by adding one to each of its digits.
num = 0
rem = 0
base = 1
while n > 0:
    rem = n % 10
    n = n // 10
    if 0 <= rem <= 8:
        rem = rem + 1
    else:
        rem = 0
    num = rem * base + num
    base = base * 10

# Printing output:
print("A new number by adding one to each of its digits:", num)

#Output:-
#Enter 5 digit number: 56437
#A new number by adding one to each of its digits: 67548