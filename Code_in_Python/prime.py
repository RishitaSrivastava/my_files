"""Q36. Write a program to print all prime numbers from 1 to 300.
(Hint: Use nested loops, break and continue) """

for Number in range(1, 301):
    count = 0
    for i in range(2, (Number // 2 + 1)):
        if Number % i == 0:
            count = count + 1
            break

    if count == 0 and Number != 1:
        print("%d" %Number, end=", ")

#Output:-
"""2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
  151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,"""