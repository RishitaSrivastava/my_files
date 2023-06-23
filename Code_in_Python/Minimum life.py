year = 0
inv = 0
alinv = 1
while alinv > inv:
    year = year + 1
    alinv = 120 * year
    inv = (year * 1000)-4000

print("Minimum life of the machine is %d years" %year)

#Output: Minimum life of the machine is 5 years