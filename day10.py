def add (n1,n2):
    return n1 +n2

def subtract (n1,n2):
    return n1 -n2

def divide (n1,n2):
    return n1 /n2

def multiple (n1,n2):
    return n1 * n2

operation = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiple
}
def calculator():
    num1 = float(input("number : "))
    for sign in operation:
        print(sign)
    should_continue = True
    while should_continue:
    
        operation_sign = input("pick an operator: ")
        num = float(input("number : "))
        calculation_symbol = operation[operation_sign]
        ans1 = calculation_symbol(num1, num)
        print(f"{num1} {operation_sign} {num} = {ans1}")
        if input("do you want to continue type y continue n to stop") == "y":
            num1 = ans1
        else:
            should_continue = False
            calculator()
calculator()            
    # operation_sign = input("pick an operato: ")
    # num3 = int(input("number : "))
    # calculation_symbol = operation[operation_sign]
    # ans = calculation_symbol(ans1, num3)
    # print(f"{ans1} {operation_sign} {num3} = {ans}")
