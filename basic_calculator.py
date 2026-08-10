## Build and deply a basic calculator by using python basics and lambda function.

def calculator(choice, x, y):
    Add = lambda a, b: a + b
    Subtract = lambda a, b: a - b
    Multiply = lambda a, b: a * b
    Divide = lambda a, b: a / b if b != 0 else "Error: Can't divide by zero"
    Exponent = lambda a, b: a ** b

    operations = {
        1: Add,
        2: Subtract,
        3: Multiply,
        4: Divide,
        5: Exponent
    }

    if choice == 1:
        return Add(x, y)
    elif choice == 2:
        return Subtract(x, y)
    elif choice == 3:
        return Multiply(x,y)
    elif choice == 4:
        return Divide(x,y)
    elif choice == 5:
        return Exponent(x,y)
    else:
        return "Invalid choice, Try Again!!!"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_choice():
    while True:
        try:
            choice = int(input("Select operation (1-6): "))
            if choice in range(1, 7):
                return choice
            print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    print("=== Calculator ===")
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent")
        print("6. Exit")

        choice = get_choice()

        if choice == 6:
            print("Exiting calculator. Goodbye!")
            break

        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")
        result = calculator(choice, x, y)
        print(f"Result: {result}")