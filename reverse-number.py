# Without function
num = 4321
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
print(rev)


# With function
def rev_number(f_num):
    f_rev = 0
    while f_num > 0:
        f_rem = f_num % 10
        f_rev = f_rev * 10 + f_rem
        f_num = f_num // 10
    return f_rev


print(rev_number(1234))
