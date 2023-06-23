#Q28.Write a program to find the factorial value of a given number entered through the keyboard.

#Taking input
n = int(input("Enter any number to get its factorial: "))

#Logic
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("Factorial of the given number is:", factorial)

#Output:-
#Enter any number to get its factorial: 7
#Factorial of the given number is: 5040