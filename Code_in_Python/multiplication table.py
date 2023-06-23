"""Q37. Write a program to print the multiplication table of the number entered by the user.
The table should get displayed in the following form.
29 * 1 = 29
29 * 2 = 58
"""

n = int(input("Print the multiplication table of any number :"))
i = 1
pro = 1
while i < 11:
    pro = n * i
    i = i + 1
    x=i-1
    print(str(n) + " * " + str(x) + " = " + str(pro))

"""Output:-
Print the multiplication table of any number :5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
"""
