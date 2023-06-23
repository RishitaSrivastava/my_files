#2. The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in meters, feet, inches and centimeters.

km= float(input("Enter distance between two cities (in km): "))
m= km*1000
f= km*3280.84
inch= km*39370.08
cm= km*1000*1000
print("The distance in kilometers = %f" %km)
print("The distance in meters = %f" %m)
print("The distance in feet = %f" %f)
print("The distance in inches = %f" %inch)
print("The distance in centimeters = %f" %cm)

#Output:-
#Enter distance between two cities (in km): 20
#The distance in kilometers = 20.000000
#The distance in meters = 20000.000000
#The distance in feet = 65616.800000
#The distance in inches = 787401.600000
#The distance in centimeters = 20000000.000000