while True:
    operator = input("Choice an operator from this list [+ - * /] or enter to exit ")
    match operator:
        case "+":
            first_number = int(input("Enter your first number: "))
            second_number = int(input("Enter your second number: "))
            print(first_number+second_number)
        case "-":
            first_number = int(input("Enter your first number: "))
            second_number = int(input("Enter your second number: "))
            print(first_number-second_number)
        case "*":
            first_number = int(input("Enter your first number: "))
            second_number = int(input("Enter your second number: "))
            print(first_number*second_number)
        case "/":
            first_number = int(input("Enter your first number: "))
            second_number = int(input("Enter your second number: "))
            print(first_number/second_number)
        case _:
            print("Bye")
            break