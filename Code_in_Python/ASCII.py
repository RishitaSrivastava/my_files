#Q30.Write a program to print all the ASCII values and their equivalent characters using a while loop. ASCII values vary from 0 to 255.

print("ASCII\t\tCharacter")
i = 0
while i < 256:
    ch = chr(i)
    print(i, '\t', ch)
    i = i + 1