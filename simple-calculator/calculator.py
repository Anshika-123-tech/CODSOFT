# TASK 2: Simple Calculator

def calculator():
    print("=== Simple Calculator ===")

    try:
        # Take user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter choice (1/2/3/4): ")

        # Perform calculation
        if choice == "1":
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")

        elif choice == "4":
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")

        else:
            print("\nInvalid choice!")

    except ValueError:
        print("\nInvalid input! Please enter numbers only.")

# Run the calculator
calculator()

