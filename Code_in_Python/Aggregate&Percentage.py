#3. If the marks obtained by a student in five different subjects are input through the keyboard, find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be obtained by a student in each subject is 100.

P= float(input("Enter the marks (out of 100) obtained in Python: "))
PL= float(input("Enter the marks (out of 100) obtained in Python Lab: "))
DSA= float(input("Enter the marks (out of 100) obtained in Data Structure and Algorithm: "))
DE= float(input("Enter the marks (out of 100) obtained in Digital Electronics: "))
A= float(input("Enter the marks (out of 100) obtained in Analog: "))
Total = P+PL+DSA+DE+A
Percentage = Total/5
print("\nAggregate marks: %f" %Total)
print("Percentage marks: %0.2f %%" %Percentage)

#Output:-
#Enter the marks (out of 100) obtained in Python: 99
#Enter the marks (out of 100) obtained in Python Lab: 97
#Enter the marks (out of 100) obtained in Data Structure and Algorithm: 96
#Enter the marks (out of 100) obtained in Digital Electronics: 98
#Enter the marks (out of 100) obtained in Analog: 90
#
#Aggregate marks: 480.000000
#Percentage marks: 96.00 %