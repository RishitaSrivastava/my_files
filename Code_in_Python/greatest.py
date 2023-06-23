#Q27. Write a program to find the greatest of the three numbers entered through the keyboard using conditional operators.

# Taking input:-
a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
c = int(input("Enter the 3rd number:"))

#Conditional operators to determine the greatest of the three.
mx = (a if (a > b and a > c) else
     (b if (b > a and b > c) else c))
print("Largest number among " + str(a) + ", " + str(b) + " and " + str(c) + " is " + str(mx))

#Output:-
#Enter the 1st number:6
#Enter the 2nd number:9
#Enter the 3rd number:2
#Largest number among 6, 9 and 2 is 9