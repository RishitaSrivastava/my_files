#Q29.Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of other.

#Takng input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number(to the power of 1st number): "))

#Printing output
print(str(a) +" to the power " +str(b)+ " is", a ** b)


#Output:-
#Enter the first number: 3
#Enter the second number(to the power of 1st number): 4
#3.0 to the power 4.0 is 81.0