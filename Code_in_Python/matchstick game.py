"""Q32.32. Write a program for a matchstick game being played between the computer and a user.
Your program should ensure that the computer always wins. Rules for the game are as follows:
- The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
- After the person picks, the computer does its picking.
- Whoever is forced to pick up the last matchstick loses the game.
- There are 21 matchsticks."""

matchsticks = 21
while matchsticks > 1:
    x = int(input("Enter the no. of matchsticks you want(1-4): "))
    comc = 5 - x
    print("Computer chooses {0} matchsticks".format(comc))
    matchsticks = matchsticks - x - comc
    print("Remaining matchsticks:", matchsticks)
if matchsticks == 1:
    x = int(input("Enter the no. of matchsticks you want(1-4): "))
    if x == 1:
        print("You lost!!!")
    if x > 1:
        print("Only 1 matchstick is left. You can choose only 1 matchstick.")
        x = int(input("Enter the no. of matchsticks you want(1-4): "))
        if x == 1:
            print("You lost!!!")


"""Output:-
Enter the no. of matchsticks you want(1-4): 1
Computer chooses 4 matchsticks
Remaining matchsticks: 16
Enter the no. of matchsticks you want(1-4): 4
Computer chooses 1 matchsticks
Remaining matchsticks: 11
Enter the no. of matchsticks you want(1-4): 3
Computer chooses 2 matchsticks
Remaining matchsticks: 6
Enter the no. of matchsticks you want(1-4): 4
Computer chooses 1 matchsticks
Remaining matchsticks: 1
Enter the no. of matchsticks you want(1-4): 2
Only 1 matchstick is left. You can choose only 1 matchstick.
Enter the no. of matchsticks you want(1-4): 1
You lost!!!
"""