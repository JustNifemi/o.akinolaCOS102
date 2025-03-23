#function explaining why I didn't solve for cubic & quartic
def others():
    print("I am currently unable to perform this function.")
    why = int(input("""
Would you like to know why?
1. Yes!
2. No!
 """))
    if why == 1:
        print("Well... I couldn't find a reasonable (enough) formula and numpy was not numpy-ing. So yeah...")
        print("At least I tried. I mean, I really did.")
    elif why == 2:
        print("Okay! But just so you know, I tried.")

#function to find the roots of a quadratic equation
def quadratic():
    print("General formula -> ax^2 + bx + c = 0")
    #collecting input for values of a, b, and c
    a = float(input("Input value for a: "))
    b = float(input("Input value for b: "))
    c = float(input("Input value for c: "))

#defining the formula for both roots (positive root & negative root)
    formula1 = (-b + (b**2 -4*a*c)**(1/2))/ (2*a)
    formula2 = (-b - (b**2 -4*a*c)**(1/2))/ (2*a)

#printing solution
    print(f"The roots of the equation {a}x^2 + {b}x + {c} are: {formula1} and {formula2}")

# Where code starts to run
print("The Root Finder (work-in-progress)")
print("""
Welcome to the root finder. 
What root would you like to find?
1. Quadratic (dregree 2)
2. Cubic (degree 3)
3. Quartic (degree 4)
4. None (you're a root hater)""")

#loop for option input and function execution
while True:
    option = input("Choose an option from 1-4 above: ")

#option is left as a string to allow for errors
#wrong input prints else

    if option == "1":
        quadratic()
    elif option == "2" or option == "3":
        others()
    elif option == "4":
        quit()
    else:
        print("Why are you trying to make things hard? Start over!")