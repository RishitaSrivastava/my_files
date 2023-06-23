#Q12. In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of literate men is 35 of the total population, write a program to find the total number of illiterate men and women if the population of the town is 80,000.
# In a town
population = 80000

# the percentage of men is 52, thus Population of mens are:-
men = 0.52 * population

# Population of women are:-
women = 0.48 * population

# Total percentage of literate men is 35 of the total population
litmen = 0.35 * population

# Total illitrate men:-
illmen = men - litmen

# The percentage of total literacy is 48.
totallit = population * 0.48

# 35 % of them are men.
# Total litrate women:-
litwomen = totallit - litmen

# Total illitrate women:-
illwomen = women - litwomen

#Printing the output:-
print("The total number of illiterate men and women if the population of the town is 80,000 are", illwomen + illmen)
 
#Output:-
#The total number of illiterate men and women if the population of the town is 80,000 are 41600.0