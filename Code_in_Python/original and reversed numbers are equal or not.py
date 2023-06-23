#Q20. A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.

# Taking five digit number as input through the keyboard:-
n = int(input("Enter a five digit number: "))
original = n

# Reversing the number.
reverse = 0
while n > 0:
    rem = n % 10
    reverse = (10 * reverse) + rem
    n = n // 10

print("Reverse of entered number is", reverse)

# Checking whether the original and reversed numbers are equal or not.
if original == reverse:
    print("The original and reversed numbers are equal!")
else:
    print("The original and reversed numbers are not equal!")
    
    
#Output:-
#Enter a five digit number: 34526
#Reverse of entered number is 62543
#The original and reversed numbers are not equal!
#
#Enter a five digit number:12321
#Reverse of entered number is  12321
#The original and reversed numbers are equal!