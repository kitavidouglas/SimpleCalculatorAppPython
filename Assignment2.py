#NAME - KITAVI DOUGLAS KIMANI
#REG NO. - SCT211-0085/2022

from datetime import datetime

#QUESTION 1 
# Main program loop
while True:
    # Display menu
    print("\nOptions:")
    print("Enter 'calculate' to calculate age")
    print("Enter 'quit' to end the program")

    # User input
    Option_Chose = input(": ")

    # Check if the user wants to quit
    if Option_Chose == "quit":
        print("Goodbye!")
        break

    # Check if the user wants to calculate age
    elif Option_Chose == "calculate":
        birth_year = int(input("Enter your birth year: "))
        birth_month = int(input("Enter your birth month: "))
        birth_day = int(input("Enter your birth day: "))

        # Get the current date
        current_date = datetime.now()

        # Calculate age
        birth_date = datetime(birth_year, birth_month, birth_day)
        age = current_date - birth_date
        

        # Extract years and days from the age difference
        years = age.days // 365  #// is is the floor division operator
        days_remaining = age.days % 365

        # Calculate months from the remaining days
        months = days_remaining // 30
        days = days_remaining % 30

        # Display the result
        print(f"Your age is {years} years, {months} months, and {days} days.")
        
    else:
        print("Invalid input. Please try again.")


#QUESTION 2
#A tip is money a customer leaves for an employee over the amount due for the goods sold or services rendered.

# Get user input for total bill, tip percentage, and number of people
bill_summation = float(input("Enter your total bill amount: Ksh"))
tip_percentage = int(input("Enter the tip percentage you wish to offer (10, 12, or 15): "))
NumberOfpeople = int(input("Enter the number of people splitting the bill: "))

# Check for invalid inputs
if tip_percentage not in [10, 12, 15] or bill_summation <= 0 or NumberOfpeople <= 0:
    print("Invalid input. Please enter valid values.")
else:
    # Calculate tip amount
    tip_amount = (bill_summation * tip_percentage) / 100

    # Calculate total amount including tip
    total_amount = bill_summation + tip_amount

    # Calculate amount per person
    amount_per_person = total_amount / NumberOfpeople

    # Display the result rounded to two decimal points
    print(f"Therefore each person  pay: Ksh{amount_per_person:.2f}")


#PART B 
'''
CONTROL FLOW
Control flow in coding refers to the order in which instructions or statements are executed in a program.
common control flow elements in programming:
1.Sequential Execution
2.Conditional statements
3.Loops
4.Switch statements
5.Function calls
'''

#QUESTION 3
#A BMI calculator
# Get user input for weight (in kilograms) and height (in meters)
Your_Weight = float(input("Enter your weight in kilograms: "))
Your_Height = float(input("Enter your height in meters: "))

# Calculate BMI
BMI = Your_Weight/ (Your_Height * Your_Height)

# Determine whether you're Underweight,Overweight or Normal weight
if BMI< 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 24.9:
    category = "Normal weight"
else:
    category = "Overweight"

# Display the BMI and weight category
print(f"Your BMI is: {BMI:.2f}")
print(f"You are categorized as: {category}")


#QUETION 4
'''
 Leap years are generally divisible by 4 BUT there is an exception for for years that are divisible by 100. 
 If a year is divisible by 100 but not by 400, it is not a leap year.
 
'''
# Get user input for the year
year = int(input("Enter a year: "))

# Check if it's a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
