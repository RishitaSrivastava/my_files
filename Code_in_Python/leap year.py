#Q26.Write a program using conditional operators to determine whether a year entered through the keyboard is a leap year or not.

#Taking input
year = int(input('Enter any year: '))

#Conditional operator
if year % 400 == 0 or (year % 4 == 0) and (year % 100 != 0):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")


#Output:-
#Enter any year: 2006
#Entered year is not a leap year

#Enter any year: 2020
#Entered year is a leap year