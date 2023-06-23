#Q19. According to the Gregorian calendar, it was Monday on the date 01/01/1900. If any year is input through the keyboard write a program to find out what is the day on 1 January of this year. """

#Take input
inp = int(input("Enter any year after 1900: "))

# Calculating the total years between 1900 and input year.
year = int(inp - 1901)

# Calculating the number of leap year.
leap_year = int(year / 4)

# Calculating the number of  non-leap year.
remaining_year = int(year - leap_year)

# Calculating the total number of days.
total_days = int((remaining_year * 365) + (leap_year * 366) + 1)

# Calculating the corresponding days.
day = int(total_days % 7)
if day == 0:
    print("Monday")
elif day == 1:
    print("Tuesday")
elif day == 2:
    print("Wednesday")
elif day == 3:
    print("Thursday")
elif day == 4:
    print("Friday")
elif day == 5:
    print("Saturday")
elif day == 6:
    print("Sunday")
else:
    print("Wrong Entry")
    
#Output:-
#Enter any year after 1900: 1908
#Wednesday