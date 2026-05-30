import math

def show_menu():
    print("\n" + "=" * 35)
    print("ADVANCED CALCULATOR")
    print("=" * 35)
    print("1:- Addition")
    print("2:- Subtraction")
    print("3:- Multiplication")
    print("4:- Division")
    print("5:- Power")
    print("6:- Modulus")
    print("7:- Square Root")
    print("8:- Exit")
    print("=" * 35)

while True:
    show_menu()
    choice = input("Enter your choice (1-8): ")
    if choice == "8":
        print("\nThank you for using the calculator!")
        break
    elif choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == "1":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "2":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "3":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "4":
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
            elif choice == "5":
                result = num1 ** num2
                print(f"Result: {num1}^{num2} = {result}")
            elif choice == "6":
                result = num1 % num2
                print(f"Result: {num1} % {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    elif choice == "7":
        try:
            num = float(input("Enter a number: "))
            if num < 0:
                print("Square root of a negative number is not possible.")
            else:
                result = math.sqrt(num)
                print(f"Square Root of {num} = {result}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice! Please select between 1 and 8.")