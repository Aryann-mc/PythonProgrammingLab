#Simple calculator program
#math module is not used
while True:
    try:
        choice = int(input(
            "Calculator program\n"
            "1. Add\n"
            "2. Subtract\n"
            "3. Multiply\n"
            "4. Divide\n"
            "5. Modulus (%)\n"
            "6. Double divide (//)\n"
            "7. Square root (sqrt)\n"
            "8. Power\n"
            "9. Exit\n"
            "Enter your choice: "
        ))
    except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

    if choice == 1:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        total = a + b
        print("Sum:", total)

    elif choice == 2:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        sub = a - b
        print("Subtract:", sub)

    elif choice == 3:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        product = a * b
        print("Product:", product)

    elif choice == 4:
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter another number: "))
            quotient = a / b
            print("Division:", quotient)
        except ZeroDivisionError:
            print("Division Error!\nNumbers can't be divided by 0")
        except ValueError:
            print("Please enter valid whole numbers.")

    elif choice == 5:
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter another number: "))
            mod = a % b
            print("Modulus:", mod)
        except ZeroDivisionError:
            print("Modulus Error!\nNumbers can't be divided by 0 and hence no remainder")
        except ValueError:
            print("Please enter valid whole numbers.")

    elif choice == 6:
        try:
            a = int(input("Enter a number: "))
            b = int(input("Enter another number: "))
            ddquotient = a // b
            print("Double division:", ddquotient)
        except ZeroDivisionError:
            print("Division Error!\nNumbers can't be divided by 0")
        except ValueError:
            print("Please enter valid whole numbers.")

    elif choice == 7:
        try:
            a = int(input("Enter a number: "))
            if a < 0:
                print("Square root of a negative number can't be found.")
            elif a == 0:
                print("Square root of 0 is: 0")
            else:
                sqrt = a ** 0.5
                print(f"Square root of {a} is: {sqrt}")
        except ValueError:
            print("Please enter a valid whole number.")

    elif choice == 8:
        try:
            base = int(input("Enter the base number: "))
            power = int(input("Enter the power of the number: "))
            result = base ** power
            print(f"The result of base {base} with power {power} is: {result}")
        except ValueError:
            print("Please enter valid whole numbers.")

    elif choice == 9:
        print("Thank you for using this program")
        break

    else:
        print("Invalid choice")




