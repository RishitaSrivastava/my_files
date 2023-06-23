#Q17. Any integer is input through the keyboard. Write a program to find out whether it is an odd number or even number."""

#Taking input.
n = int(input("Enter a number to check whether it is an Even or a Odd : "))

#Logic
if n % 2 == 0:
    print("Entered number is even!")
else:
    print("Entered  number is odd!")
       
#Output:-
#Enter a number to check whether it is an Even or a Odd : 7
#Entered  number is odd!
#
#Enter a number to check whether it is an Even or a Odd : 2
#Entered number is even!