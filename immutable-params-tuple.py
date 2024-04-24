# 19/4/24
# AIM: WAP to demonstrate the mutability of a parameter when a tuple is passed in and converted to a list
# in the function.

def calc(a):
    a = list(a)
    a[0] = a[0] * 2
    a[1] = a[1] + 1
    print("Calc:", a)


P = (1, 2)
print("Tuple before function: ", P)
calc(P)                                     # outputs list
print("Tuple after function: ", P)          # tuple is unchanged
