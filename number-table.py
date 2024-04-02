# 20/3/24
# AIM: WAP to print till nth multiple of a given number

num = int(input("Enter number: "))
n = int(input("Enter no. of multiples: "))

# Without function
for i in range(1, n + 1):
    print(f"{num} × {i} = {num * i}")


# With function
def table(f_num, f_n):
    for f_i in range(1, f_n + 1):
        print(f"{f_num} × {f_i} = {f_num * f_i}")


print()

table(num, n)
