a,o,b = input().split()
a = int(a)
b = int(b)

def add(a,b):
    return a + b 

def minus(a,b):
    return a - b

def multiple(a,b):
    return a * b


def divide(a,b):
    return int(a / b)






def print_expression(a,o,b):

    if o not in ["+", "-", "*", "/"]:
        return False

    if o == "+":
        x = add(a,b)
    elif o == "-":
        x = minus(a,b)
    elif o == "*":
        x = multiple(a,b)
    elif o == "/":
        x = divide(a,b)

    print(f"{a} {o} {b} = {x}")



print_expression(a,o,b)