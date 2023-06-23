#Q13. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer."""

#Taking the amount to be withdrawn is input through the keyboard in hundreds.
amount = int(input("Enter the amount to withdraw: "))

#Calculation
ten = amount // 10
fifty = amount // 50
hundred = amount // 100

# Printing Output
print("The total number of currency notes of each denomination the cashier will have to give to the withdrawer:")
print("10 :", ten)
print("50 :", fifty)
print("100 :", hundred)

#Output:-
#Enter the amount to withdraw:1400
#The total number of currency notes of each denomination the cashier will have to give to the withdrawer.
#10:  140
#50:  28
#100:  14