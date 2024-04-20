# 18/4/24
# AIM: WAP to demonstrate the mutability of a parameter when a list is passed in.

def calc(a):
    a[0] = a[0] * 2
    a[1] = a[1] + 1
    print("Calc:", a)


P = [1, 2]
print("List before function: ", P)
calc(P)                                 # outputs list
print("List after function: ", P)       # list is changed
