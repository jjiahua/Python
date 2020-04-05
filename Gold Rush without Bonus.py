# This program was created on 4/4/20 by Jiahua Huang
# This program is a game dubbed Gold Rush.
# It is a game of chance where the player has
# to last long weeks betting on their chances to earn money.
from random import *

# Total money in the bank at the beginning of the game
amount = 3000
#  Supply cost weekly
supplyCostWeekly = 500

print("Your amount is:" + " $" + str(amount))

week = 0
count = 1
# a trigger for invalid input.
# False is active since there are no invalid inputs initially.
invalid_input = False

while True:
    # Check if the remainder of the money is enough to continue the game.
    if amount < supplyCostWeekly:
        print("Sorry, you do not have enough money to play. Your amount of cash is: $" + str(
            amount) + " You lasted for " + str(week) + " weeks.")
        print("Game Over!!!")
        break
    if invalid_input is False:
        # every time there is an input, resembles the beginning of a new week
        print("Week " + str(count))
        # Display the total money in the bank; Get user site option input
        print("--------------Bank: $" + str(amount) + " --------------")
        print("Please chose your site by enter digit 1, 2 or 3.")
        print("1: Lucky Clover.")
        print("2: Diamond Mine. ")
        print("3: Hearts are wild")
        print("Note that a string input other than 1, 2, or 3 will result the loss of your desire to play the game. "
              "Otherwise, if you accidentally type an invalid integer, the program will ask again.")
        print("Once you have entered an input, it will begin your week.")

    try:
        # idea is straight forward based on what's read on the print function above
        siteDecision = int(input())
        if 0 < siteDecision <= 3:
            count = count + 1
            week = week + 1
            amount = amount - supplyCostWeekly
            invalid_input = False
    except ValueError:
        print("Your current desire to play the game is lost. The game has ended.\n Your amount of cash is: $" + str(
            amount) + " You lasted for " + str(week) + " weeks.")
        print("Game Over!!!")
        break
    # money taken away at the beginning of each week

    chance = randint(1, 10)
    if siteDecision == 1:  # Lucky Clover
        # Get a rand number between 1 and 10 inclusive. Use rand number to get the probability

        # 10% chance at $1000 payload
        if chance == 1:
            amount = amount + 1000
            print("Congratulations, you increased $1000!")
            print("Your bank amount is:" + " $" + str(amount))
        elif chance < 5:
            amount = amount + 500
            print("You increased $500!")
            print("Your bank amount is:" + " $" + str(amount))
        else:
            amount = 1 / 2 * amount
            print("You lost half of your money to a thief. He stole $" + str(amount))
            print("Your bank amount is:" + " $" + str(amount))

    elif siteDecision == 2:  # Diamond Mine

        if chance <= 2:
            # The purpose of the code is found on the print statements.
            amount = amount + 800
            print("Congratulations, you increased $800!")
            print("Your bank amount is:" + " $" + str(amount))
        elif chance <= 6:
            amount = amount + 400
            print("You earned $400!")
            print("Your bank amount is:" + " $" + str(amount))
        else:
            if supplyCostWeekly == 500:
                amount = amount - 200
                supplyCostWeekly = 700
            print(
                "If this is the first time you are viewing this message,"
                " 200 dollars have been deducted from your bank. "
                "Now, the supply cost is $700 weekly from now on.")
            print("Your bank amount is:" + " $" + str(amount))

    # Hearts are Wild
    elif siteDecision == 3:
        if chance == 1:
            amount = amount + 8000
            print("Incredible, you just earned 8000 dollars")
            print("Your bank amount is:" + " $" + str(amount))

        elif chance < 4:
            amount = amount + 300
            print("You earned 300 dollars!")
            print("Your bank amount is:" + " $" + str(amount))
        else:
            print("You died!")
            print("Your bank amount you had before your death is:" + " $" + str(amount) + " You lasted for " + str(
                week) + " weeks.")
            print("Game Over!!!")
            break
    else:
        print("Invalid input. Enter Again")
        invalid_input = True
