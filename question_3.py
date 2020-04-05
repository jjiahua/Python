# This program is question 3 assignment

# The total cost for all customers
total_cost = 0

# The total number of calls for all customer
total_calls = 0

# The total minutes for all calls of all customers
total_minutes = 0

# The particular customer total cost
customer_price = 0

invalid_input = False
while True:  # loop 2
    escape_loop1 = False
    escape_loop2 = False
    if invalid_input is False:
        minutes = int(input("Please input the number of minutes in a call?\n"))
    else:
        minutes = int(input())
        invalid_input = False

    if minutes > 0:
        total_calls = total_calls + 1
        total_minutes = total_minutes + minutes

        if minutes <= 3:
            price = 1.24
        else:
            price = round(1.24 + 0.76 * (minutes - 3), 2)

        customer_price = round(customer_price + price, 2)

        total_cost = round(total_cost + price, 2)

        print("Your cost is $" + str(price))

        retry = input("Do you want to call again? Y/N?")
        while True:  # loop 1
            if retry == "Y" or retry == "y":
                break
            elif retry == "N" or retry == "n":
                print("Your total price is $" + str(customer_price))
                isMore = input("Are there any more customers? Y/N")
                while True:
                    if isMore == "Y" or isMore == "y":
                        customer_price = 0
                        escape_loop1 = True
                        break
                    elif isMore == "N" or isMore == "n":
                        average_minutes_per_call = round(total_minutes / total_calls, 2)
                        print("The total number of calls:", total_calls)
                        print("The total cost for all customers: $" + str(total_cost))
                        print("The average minutes per call:", average_minutes_per_call)
                        escape_loop1 = True
                        escape_loop2 = True
                        break
                    else:
                        print("Invalid input. Please enter a correct value", end=" ")
                        isMore = input()
            else:
                print("Invalid input, Enter again.", end=" ")
                retry = input()
            if escape_loop1 is True:
                break
        if escape_loop2 is True:
            break

    else:
        print("Your input is invalid. Enter again.", end=" ")
        invalid_input = True


