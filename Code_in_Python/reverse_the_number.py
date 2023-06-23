#Q10. If a five-digit number is input through the keyboard, write a program to reverse the number.

#Taking five digit number as input through the keyboard:-
n = int(input("Enter a five digit number: "))

#Reversing the number:
reverse = 0
while n > 0:
    rem = n % 10
    reverse = (10 * reverse) + rem
    n = n // 10

#Printing Output
print("Reverse of entered number is %d" %reverse)

#Output:-
#Enter a five digit number: 43576
#Reverse of entered number is 67534