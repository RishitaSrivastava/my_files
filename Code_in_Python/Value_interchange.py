C= int(input("Enter the number for C: "))
D= int(input("Enter the number for D: "))
C= C+D  #(C:20,D:30)C=20, D=10 =>C=30
D= C-D  #C=30, D=10 =>D=20
C= C-D  #C=30, D=20 =>C=10 (C:30,D:20)
print("\nThe value of C after interchange: %d" %C)
print("The value of D after interchange: %d" %D)

#Output:-
#Enter the number for C: 8
#Enter the number for D: 6
#
#The value of C after interchange: 6
#The value of D after interchange: 8