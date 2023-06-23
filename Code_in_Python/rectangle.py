"""Q23.Find the absolute value of a number entered through the keyboard. Given the length and breadth of a rectangle
write a program to find whether the area of rectangle is greater than its perimeter."""

# Taking input.
n = float(input('Enter any number to get its absolute value: '))

# Logic to find absolute value.
if n < 0:
    absolute = n- (2 * n)
else:
    absolute = n
print('Absolute value of given number is:', absolute)

# Taking input to check whether the area of rectangle is greater than its perimeter or not.
l = float(input('Enter the length of rectangle: '))
b = float(input('Enter the breadth of rectangle: '))

area = l * b
perimeter = 2 * (l+ b)

if area > perimeter:
    print('Area of rectangle is greater than its perimeter.')
elif area < perimeter:
    print('Area of rectangle is not greater than its perimeter.')


#Output:-
#Enter any number to get its absolute value: 23
#Absolute value of given number is: 23.0
#Enter the length of rectangle: 9
#Enter the breadth of rectangle: 4
#Area of rectangle is greater than its perimeter.