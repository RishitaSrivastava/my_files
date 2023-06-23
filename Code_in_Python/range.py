"""Q35. Write a program to find the range of a set of numbers.
Range is the difference between the smallest and biggest number in the list."""

n = int(input("How many numbers you want to enter: "))
l = []
for i in range(n):
    x = int(input("Enter a number: "))
    l.append(x)
ma = max(l)
mi = min(l)
print("The range(maximum of list - minimum of list) of given set of numbers is:", ma - mi)

"""output:-
How many numbers you want to enter: 3
Enter a number: 6
Enter a number: 1
Enter a number: 9
The range(maximum of list - minimum of list) of given set of numbers is: 8
"""
