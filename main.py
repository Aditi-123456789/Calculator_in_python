def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Available operations: +, -, *, /")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator.")
                continue

            print("Result: ", result)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print("An error occurred:", str(e))

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the Python Calculator!")
            break

if __name__ == "__main__":
    calculator()

