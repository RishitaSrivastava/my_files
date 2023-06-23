#Q25.Using conditional operators determine:
#(i)Whether the character entered through the keyboard is lower-case alphabet or not.
#(ii)Whether the character entered through the keyboard is special character or not.

#TAKING INPUT
c = input("Enter any character: ")
ch = ord(c[0])

if 97 <= ch <= 122:
    print("Entered character is lowercase alphabet!")
elif 32 <= ch <= 47 or 58 <= ch <= 64 or 123 <= ch <= 126:
    print("Entered character is special character!")
else:
    print("Entered character is neither lower-case alphabet nor special character!")

#Output:-
#Enter any character: k
#Entered character is lowercase alphabet!

#Enter any character: A
#Entered character is neither lower-case alphabet nor special character!

#Enter any character: #
#Entered character is special character!