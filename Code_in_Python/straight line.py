#Q24.Given three points (x1,y1), (x2,y2) and (x3,y3), write a program to check if all the three points fall on one straight line."""

#Taking input
x1 = float(input('Enter the value of x1: '))
y1 = float(input('Enter the value of y1: '))
x2 = float(input('Enter the value of x2: '))
y2 = float(input('Enter the value of y2: '))
x3 = float(input('Enter the value of x3: '))
y3 = float(input('Enter the value of y3: '))

#For straight line
a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
if a == 0:
    print("Entered three points fall on same straight line.")
else:
    print("Entered three points do not fall on same straight line.")


#Output:-
#Enter the value of x1: 1
#Enter the value of y1: 5
#Enter the value of x2: 3
#Enter the value of y2: 2
#Enter the value of x3: 4
#Enter the value of y3: 8
#Entered three points do not fall on same straight line.
#-----------------------------------------------------------------
#Enter the value of x1: 2
#Enter the value of y1: 3
#Enter the value of x2: 4
#Enter the value of y2: 7
#Enter the value of x3: 6
#Enter the value of y3: 11
#Entered three points fall on same straight line.