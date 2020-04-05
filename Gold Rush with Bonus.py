# This program was created on 4/4/20 by Jiahua Huang
# This program is a game dubbed Gold Rush.
# It is a game of chance where the player has
# to last long weeks betting on their chances to earn money.
from random import *

# The code is straightforward and internal comments from the code without Bonus
# should make the idea clear

# Total money in the bank at the beginning of the game
amount = 3000
#  Supply cost weekly
supplyCostWeekly = 500

print("Your amount is:" + " $" + str(amount))

week = 0
count = 1
# random choice of a thief
thieves = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
totalMoneyBorrowed = 0
interestRate = 0.3
interest = 0
invalid_input = False
while True:

    # Display
    print("Week " + str(count))
    print("*Bank: $" + str(round(amount, 2)))
    print("*Borrowed: $" + str(round(totalMoneyBorrowed, 2)))
    print("*Interest: $" + str(round(interest, 2)))
    print("************************************************************************************************")

    print("Enter the amount you want to borrow from the bank, the maximum amount is $500, interest rate is 30% weekly")
    while True:
        # application of borrowing money
        moneyBorrowed = int(input())
        if moneyBorrowed > 500 or moneyBorrowed < 0:
            print("Invalid Input. Enter again.")
        else:
            totalMoneyBorrowed = totalMoneyBorrowed + moneyBorrowed
            amount = amount + moneyBorrowed
            break

    if amount < supplyCostWeekly:
        amount = round(amount, 2)
        print("Sorry, you do not have enough money to play. Your amount of cash is: $" + str(
            amount) + " You lasted for " + str(week) + " weeks.")
        print("Game Over!!!")
        break
    print("--------------Bank: $" + str(amount) + " --------------")
    print("Please chose your site by enter digit 1, 2 or 3.")
    print("1: Lucky Clover.")
    print("2: Diamond Mine. ")
    print("3: Hearts are wild")
    print("Note that a string input other than 1, 2, or 3 will result the loss of your desire to play the game. "
          "Otherwise, if you accidentally type an invalid integer, the program will ask again.")
    print("Once you have entered an input, it will begin your week.")

    try:
        while True:
            siteDecision = int(input())
            if siteDecision > 3 or siteDecision <= 0:
                print("Invalid input. Enter Again.")
            else:
                count = count + 1
                week = week + 1
                amount = amount - supplyCostWeekly
                break
    except ValueError:
        print("Your current desire to play the game is lost. The game has ended.\n Your amount of cash is: $" + str(
            amount) + " You lasted for " + str(week) + " weeks.")
        print("Game Over!!!")
        break

    # Get a rand number between 1 and 10 inclusive. Use rand number to get the probability

    chance = randint(1, 10)
    if siteDecision == 1:  # Lucky Clover

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
            # pick a thief option from list
            thiefOption = randint(0, 9)
            moneyLose = round(amount * thieves[thiefOption], 2)
            amount = amount - moneyLose
            print("Thief steal $" + str(moneyLose))
    elif siteDecision == 2:  # Diamond Mine

        if chance <= 2:
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
    else:
        if chance == 1:
            amount = amount + 8000
            print("Incredible, you just earned 8000 dollars")
            print("Your bank amount is:" + " $" + str(amount))

        elif chance < 4:
            amount = amount + 300
            print("You earned 300 dollars!")
            print("Your bank amount is:" + " $" + str(amount))
    # naturally, interest needs to be calculated
    interest = round(totalMoneyBorrowed * interestRate, 2)
    amount = amount - interest
