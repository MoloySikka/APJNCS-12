# 19/4/24
# AIM: WAP to demonstrate the immutability of a parameter when an integer is passed in.

def calc(a, b):
    a = a * 2
    b = b + 1
    print("Calc:", a, b)


P, Q = 100, 200
print("Values before function: ", P, Q)
calc(P, Q)                              # outputs integers
print("Values after function: ", P, Q)      # values remain unchanged
