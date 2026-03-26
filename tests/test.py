# Get user input
change_due = int(input())

if change_due <= 0:
    print("No change")
else:
    denominations = [
        ("Dollar", "Dollars", 100),
        ("Quarter", "Quarters", 25),
        ("Dime", "Dimes", 10),
        ("Nickel", "Nickels", 5),
        ("Penny", "Pennies", 1),
    ]

    for singular, plural, value in denominations:
        count = change_due // value
        change_due %= value

        if count > 0:
            if count == 1:
                print(count, singular)
            else:
                print(count, plural)

    x = None
    while x and False: