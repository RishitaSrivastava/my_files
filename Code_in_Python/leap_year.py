#18. Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not. (Hint: Use the % (modulus) operator)"""

# Taking input.
year = int(input("Enter any year to check whether it is leap year or not: "))

#For determine whether the year is a leap year or not.
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("%d is a leap year" %year)
        else:
            print("%d is not a leap year" %year)
    else:
        print("%d is a leap year" %year)
else:
    print("%d is not a leap year" %year)
    
#Output:-
#Enter any year to check whether it is leap year or not: 2008
#2008 is a leap year