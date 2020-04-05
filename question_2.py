# 2. Entrance fees for school plays vary with age. Create a program that will generate a bill for the
# # groups entering the play.
# # o Children under 12 cost $0.50, students under 18 cost $2.50, adults are $5.00 and senior
# # citizens (over 65) are $0.75.
# # o For each group, you will ask for each person’s age.
# # o At the end of each group, display the total cost of the bill, as well as the total cost in
# # each age category.
# # o Make it work for more than one group (similar to question #1).
# # o When there are no more groups, output the total number of people attending the play
# # and the total revenue.

revenue = 0
total_number_of_people_in_play = 0
children_price = 0
student_price = 0
adult_price = 0
senior_price = 0
total_cost = children_price + student_price + adult_price + senior_price
group = input("Welcome to Markville's school play. Press Enter to add a group to the play")
invalid_input = False
escape_loop1 = False
while True:
    if invalid_input is False:
        age = int(input("What is your age: "))

    else:
        age = int(input())
        invalid_input = False

    if 0 < age < 12:
        total_number_of_people_in_play = total_number_of_people_in_play + 1
        children_price = children_price + 0.50
    elif 12 <= age < 18:
        total_number_of_people_in_play = total_number_of_people_in_play + 1
        student_price = student_price + 2.50
    elif 18 <= age <= 65:
        total_number_of_people_in_play = total_number_of_people_in_play + 1
        adult_price = adult_price + 5.00
    elif 65 < age < 125:
        total_number_of_people_in_play = total_number_of_people_in_play + 1
        senior_price = senior_price + 0.75
    else:
        print("Invalid input. Enter again.", end=" ")
        invalid_input = True
    if invalid_input is False:
        # loop 1
        while True:
            if escape_loop1 is True:
                escape_loop1 = False
                break
            if invalid_input is False:
                is_more = input("Are there any more people in your group (Y/N)? ")
            else:
                is_more = input()
                invalid_input = False
            if is_more == "Y" or is_more == "y":
                break
            elif is_more == "N" or is_more == "n":
                total_cost = children_price + student_price + adult_price + senior_price
                print("The total cost is $" + str(total_cost) + ".")
                print("The cost for the child's category is $" + str(children_price) + ".")
                print("The cost for the student's category is $" + str(student_price) + ".")
                print("The cost for the adult's category is $" + str(adult_price) + ".")
                print("THe cost for the senior's category is $" + str(senior_price) + ".")
                revenue = revenue + total_cost
                children_price = 0
                student_price = 0
                adult_price = 0
                senior_price = 0

                while True:

                    if invalid_input is False:
                        more_group = input("Are there any more groups (Y/N)? ")
                    else:
                        more_group = input()
                        invalid_input = False
                    if more_group == "Y" or more_group == "y":
                        escape_loop1 = True
                        break

                    elif more_group == "N" or more_group == "n":
                        print("Number of audience member(s) entering the play is", total_number_of_people_in_play)
                        print("The revenue is $" + str(revenue) + ".")
                        quit()
                    else:
                        print("Invalid input. Enter again.", end=" ")
                        invalid_input = True
            else:
                print("Invalid input. Enter again.", end=" ")
                invalid_input = True




