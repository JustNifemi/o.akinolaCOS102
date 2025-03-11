print("Financial Calculator")
#getting input for user's  name
name = input("What is your name? ")
print(f"Hello {name}! Welcome to the financial calculator.")
# defining options
print("""Available formulas:
1. Simple Interest
2. Compound Interest
3. Annuity Plan
4. None (quit)""")

formula = int(input("What formula would you like to calculate (1-4)? "))

# defining formulas and variables
if formula == 1:
    #defining variables
    principal = int(input("Input principal(P): "))
    rate = int(input("Input rate(r): "))
    time = int(input("Input time(t) in years: "))

    #defining formula for simple interest
    simple_interest = principal * (1 + (rate/100) * time)
    print(f"Simple interest(A) is: {simple_interest}")