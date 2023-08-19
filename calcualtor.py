while True:
    print("Calculator time")
    print("What's your first number")
    first_number = int(input())
    print("What's your second number")
    second_number = int(input())
    print("Enter an operator(+, -, *, /)")
    while True:
        Operator = input()
        if Operator == "+":
            answer = (first_number + second_number)
            print(first_number, Operator, second_number, "=", answer)
            break
        elif Operator == "-":
            answer = (first_number - second_number)
            print(first_number, Operator, second_number, "=", answer)
            break
        elif Operator == "*":
            answer = (first_number * second_number)
            print(first_number, Operator, second_number, "=", answer)
            break
        elif Operator == "/":
            answer = (first_number / second_number)
            print(first_number, Operator, second_number, "=", answer)
            break
        else:
            print("Input a valid operator")
            continue
    break
        
