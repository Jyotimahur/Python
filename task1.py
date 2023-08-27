#Python program to make a simple calculator usin functions....
# Addition of two numbers...
def add(x, y):
    return x + y

#Subtraction two numbers...
def subtract(x, y):
    return x - y

# Multiplication of two numbers...
def multiply(x, y):
    return x * y

# Division of two numbers...
def divide(x, y):
    return x / y

#Print the operations...
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Using loop...
while True:

# Take input from the user...
    choice = input("Enter choice(1/2/3/4):")

# check if choice is one of the four options....
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
 # check if user wants another calculation...
# break the while loop if answer is no...
        next_calculation = input("Let's begin the next Calculation?(yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")