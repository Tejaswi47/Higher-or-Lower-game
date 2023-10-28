# Higher or lower game.
# Let us assume, User given a number and the computer have to say that the number
# lies in between the two numbers(1-100).
# then the User or player guessed the correct number
# At last he wins.
import random

# Taking a list of 100 numbers.
Computer_Choice = []
for i in range(1, 101):
    Computer_Choice.append(i)
Computer_Picked = random.choice(Computer_Choice)

# Game code starts from here
attempts = 0
Game_is_on = True
while Game_is_on:
    Number = int(input("Enter the number"))
    attempts += 1
    if Number == Computer_Picked:
        print(f"You have Won the game by {attempts} ")
        Game_is_on = False
    elif Number < Computer_Picked:
        print("Lower, Guess greater number")
    elif Number > Computer_Picked:
        print("Greater, Guess Lower number")
