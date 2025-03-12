print("Financial Calculator")
#getting input for user's  name
name = input("What is your name? ")
print(f"Hello {name}! Welcome to the financial calculator.")

while True:
    # defining options and input
    print("""Available formulas:
    1. Simple Interest
    2. Compound Interest
    3. Annuity Plan
    4. None (quit)""")

    formula = input("What formula would you like to calculate (1-4)? ")

    # defining formulas and variables
    if formula == "1":
        # defining variables
        principal = float(input("Input principal amount(P): "))
        rate = float(input("Input rate(r): "))
        time = float(input("Input time(t) in years: "))

        # defining formula for simple interest
        simple_interest = principal * (1 + (rate / 100) * time)
        print(f"Simple interest(A) is: {simple_interest}")


    elif formula == "2":
        # defining variables
        principal = float(input("Input principal amount(P): "))
        rate = float(input("Input rate(r): "))
        time = float(input("Input time(t) in years: "))
        amount_of_times = float(input("Input amount of times the interest  is compounded(n): "))

        # defining formula for compound interest
        compound_interest = principal * (1 + (rate / amount_of_times)) ** (amount_of_times * time)
        print(f"Compound Interest(A) is: {compound_interest}")


    elif formula == "3":
        # defining variables
        pmt = float(input("Input payment amount per period(PMT): "))
        r = float(input("Input rate(r): "))
        t = float(input("Input time(t) in years: "))
        n = float(input("Input amount of times the interest  is compounded per year(n): "))

        # defining the formula for annuity
        annuity = pmt * (((1 + r/n)**(n*t) - 1)/(r/n))
        print(f"Annuity value is: {annuity}")


    elif formula == "4":
        print("Thank you for using the financial calculator!")
        break
    else:
        print("Unknown input. Try numbers 1-4 instead!")