"""Q33. Write a program to enter the numbers till the user wants and at the
end it should display the count of positive, negative and zeros entered."""

n = int(input("Enter the no. of times you want to give input: "))
count_0 = 0
count_negative = 0
count_positive = 0
for i in range(n):
    x = int(input("Enter the no. you want: "))
    if x == 0:
        count_0 = count_0 + 1
    if x > 0:
        count_positive = count_positive + 1
    if x < 0:
        count_negative = count_negative + 1
print("No. of zeroes are:", count_0)
print("No. of positive numbers. are:", count_positive)
print("No. of negative numbers are:", count_negative)


"""Output:-
Enter the no. of times you want to give input: 4
Enter the no. you want: -5
Enter the no. you want: 4
Enter the no. you want: 0
Enter the no. you want: 6
No. of zeroes are: 1
No. of positive numbers. are: 2
No. of negative numbers are: 1
"""
