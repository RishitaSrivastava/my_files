#Q09. If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits.

# Taking five digit number as input through the keyboard:-
n = int(input("Enter a five digit number: "))

# Calculating the sum of its digits:
sum = 0
while n > 0:
    rem = n % 10
    sum = sum + rem
    n = n // 10

# Printing Output
print("Sum of the digit are : %d" %sum)

#Output:-
#Enter a five digit number: 34526
#Sum of it's digit are : 20