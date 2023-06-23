#1. Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.

BS= float(input("Enter Ramesh basic salary : " ))
DA=0.4*BS
HR=0.2*BS
GS=BS+DA+HR
print("Basic Salary is: %f" %BS)
#print("Dearness Allowance is: %f" %DA)
#print("House Rent is: %f" %HR)
print("And the Gross Salary is: %f" %GS)

#output:-
#Enter Ramesh basic salary : 20000
#Basic Salary is: 20000.000000
#Dearness Allowance is: 8000.000000 
#House Rent is: 4000.000000
#And the Gross Salary is: 32000.000000