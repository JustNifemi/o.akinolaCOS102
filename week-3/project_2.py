#function to calutate atr 
def calc_atr():
    if years > "25" and age >= "55":
        print("The Annual Tax Revenue (ATR) for this staff is: ₦5600000")

    elif years > "20" and age >= "45":
        print("The Annual Tax Revenue (ATR) for this staff is: ₦4480000")
 
    elif years > "10" and age >= "35":
        print("The Annual Tax Revenue (ATR) for this staff is: ₦1500000")
    else:
        print("The Annual Tax Revenue (ATR) for this staff is: ₦550000")



print("Izifin's ATR calculator")
print("Welcome to  Izifin Technology's ATR calculator!")

# Get user input
years = input("Please enter staff's years of experience: ")
age = input("Please enter staff's age: ")

# Calculate ATR
calc_atr()

print("Thank you for using our program!")
