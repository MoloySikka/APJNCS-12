# 2/4/24
# AIM: WAP to create a Calculator.

# Without functions:

math_prompt = """\n\nChoose an operator:
+
-
/
*
What is your choice?: """


while True:
    oper = input(math_prompt)
    num1 = int(input("Enter first operand: "))
    num2 = int(input("Enter second operand: "))
    print()
    if oper == "+":
        ans = num1 + num2
    elif oper == "-":
        ans = num1 - num2
    elif oper == "*":
        ans = num1 * num2
    elif oper == "/":
        ans = num1 / num2
    else:
        print("Invalid")
        continue

    print(f"\n{num1} {oper} {num2} = {ans}")



# With function
    
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

def sub(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"

def mul(num1, num2):
    return f"{num1} * {num2} = {num1 * num2}"

def sub(num1, num2):
    return f"{num1} / {num2} = {num1 / num2}"


def calculator():
    global math_prompt
    oper = input(math_prompt)
    a = int(input("Enter first operand: "))
    b = int(input("Enter second operand: "))
    print()
    if oper == "+":
        print(add(a, b))
    elif oper == "-":
        print(sub(a, b))
    elif oper == "*":
        print(mul(a, b))
    elif oper == "/":
        print(div(a, b))
    else:
        print("Invalid")


while True:
    calculator()
    
    
