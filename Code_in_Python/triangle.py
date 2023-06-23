#Q22.Write a program to check whether a triangle is valid or not, when the three angles of triangle are entered through keyboard. A triangle is valid if sum of all three angles is 180 degrees.

# Taking input:-
a = float(input('Enter the 1st angle: '))
b = float(input('Enter the 2nd angle: '))
c = float(input('Enter the 3rd angle: '))

# A program to check whether a triangle is valid or not.
s = a+b+c
if s == 180:
    print('The triangle is valid.')
else:
    print('The triangle is not valid.')

#Output:-
#Enter the 1st angle: 20
#Enter the 2nd angle: 40
#Enter the 3rd angle: 80
#The triangle is not valid.
#-------------------------------------
#Enter the 1st angle: 40
#Enter the 2nd angle: 60
#Enter the 3rd angle: 80
#The triangle is valid.