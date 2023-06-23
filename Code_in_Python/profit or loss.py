#Q16. If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred."""

#Taking cost price and selling price of an item as input.
cp = int(input("Enter the cost price:"))
sp = int(input("Enter the selling price:"))

#A program to determine whether the seller has made profit or incurred loss.
#Also to determine how much profit he made or loss he incurred.
if sp > cp:
    profit = sp - cp
    print("\nSeller incurred profit!\nTotal profit made is:", profit)
else:
    loss = cp - sp
    print("\nSeller incurred loss!\nTotal loss is:", loss)
    
#Output:-
#Enter the cost price:200
#Enter the selling price:220
#
#Seller incurred profit!
#Total profit made is: 20