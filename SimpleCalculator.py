#NAME - KITAVI DOUGLAS KIMANI
#REG NO. - SCT211-0085/2022


# Get the user's name
user_name = input("Enter your name: ")


# GreetS the user 
print(f"Hello, {user_name}!")

# Initialize variables for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Provide options to the user
print("Options:")
print("Enter 'add' for addition")
print("Enter 'subtract' for subtraction")
print("Enter 'multiply' for multiplication")
print("Enter 'divide' for division")

# Get the operation choice from the user
operation = input("Enter your choice: ")

# Perform the selected operation and display the result
if operation == 'add':
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")
elif operation == 'subtract':
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif operation == 'multiply':
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif operation == 'divide':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation choice")

# End of the program
print(f"Goodbye, {user_name}!")