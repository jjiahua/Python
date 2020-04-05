# 1. Act as a cash register at Toys R’us and calculate the final cost for a purchase.
# o Every item over $10.00 requires 13% sales tax.
# o Each item for a customer will be entered in one at a time.
# o It should also work for multiple customers.
#  Must look identical to sample program below.

end_program = False
print("Welcome to Toys R’us!")
while end_program is False:
    new_customer = False
    cost = 0
    total = 0

    while new_customer is False and end_program is False:
        while True:
            item = input("What is your item? ")
            cost = float(input("How much does it cost? $"))
            if cost > 10:
                cost = cost*1.13
                break
            elif 0 <= cost <= 10:
                break
            else:
                print("Invalid input Enter again.")
        cost = round(cost, 2)
        total = total + cost
        print("Your item costs $"+str(cost))
        anymore = input("Are you buying any other toys (Y/N)? ")
        while end_program is False and new_customer is False:
            if anymore == "y" or anymore == "Y":
                break
            elif anymore == "n" or anymore == "N":
                print("Your total bill comes to $"+str(round(total, 2)))
                moreCustomers = input("Are there any other customers (Y/N)? ")
                while True:
                    if moreCustomers == "y" or moreCustomers == "Y":
                        new_customer = True
                        break
                    elif moreCustomers == "n" or moreCustomers == "N":
                        end_program = True
                        print("Thank you for shopping at Toys R’us!")
                        break
                    else:
                        moreCustomers = input("Invalid response. Enter again. ")
            else:
                anymore = input("Invalid response. Enter again. ")
