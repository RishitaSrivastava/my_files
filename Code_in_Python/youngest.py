#Q21. If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three.

# Taking input:-
ram = int(input("Enter the age of Ram: "))
shyam = int(input("Enter the age of Shyam: "))
ajay = int(input("Enter the age of Ajay: "))

#To determine the youngest of the three.
if ram < shyam and ram < ajay:
    print("Ram is youngest.")
elif shyam < ajay and shyam < ram:
    print("Shyam is youngest.")
else:
    print("Ajay is youngest.")


#Output:-
#Enter the age of Ram: 54
#Enter the age of Shyam: 60
#Enter the age of Ajay: 25
#Ajay is youngest.