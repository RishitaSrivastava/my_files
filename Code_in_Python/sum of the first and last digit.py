#Q11. If a four-digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number."""

#Taking four-digit number as input through the keyboard.
n = int(input("Enter a four digit number: "))

#Program to obtain the sum of the first and last digit of this number.
i = 1
res = 0
while n > 0:
    rem = n % 10
    if i == 1:
        i = i + 1
        res = res + rem
    n = n // 10
    if 0 < n <= 9:
        res = res + n

#Printing Output
print("The sum of the first and last digit of this number is:", res)

#Output:-
#Enter the four digit number: 5463
#The sum of the first and last digit of this number is: 8