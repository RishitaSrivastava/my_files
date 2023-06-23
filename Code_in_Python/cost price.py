#Q14. If the total selling price of 15 items and the total profit earned on them is input through the keyboard, write a program to find the cost price of one item.

# Taking input as the total selling price of 15 items and the total profit earned on them.
sp = int(input("Enter the total selling price of 15 items: "))
profit = int(input("Enter the total profit earned on them: "))

# Calculating the cost price of one item.
cp = (sp - profit) / 15

print("The cost price of one item: %0.2f" %cp)

#Output:-
#Enter the total selling price of 15 items: 1500
#Enter the total profit earned on them: 200
#The cost price of one item: 86.67