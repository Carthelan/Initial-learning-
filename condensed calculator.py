import operator
oper_dict = {
    "+": operator.add,
    "-": operator.sub,       
    "*": operator.mul,
    "/": operator.truediv,
}
while True:
    print("What's your first number")
    first_number = int(input())
    print("What's your second number")
    second_number = int(input())
    print("Enter an operator(+, -, *, /)")
    while True:
        oper = oper_dict[input()] 
        answer = oper(first_number, second_number)
        print(first_number, second_number, "=", answer)
        break
    break
