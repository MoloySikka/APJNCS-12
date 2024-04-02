# 19/3/24
# AIM: WAP to check if a given number is prime

num = int(input("Enter number to be checked: "))

# Without function

stop = int(num ** 0.5)

prime = True

for i in range(2, stop):
    if num % i == 0:
        prime = False

if prime:
    print("Prime")
else:
    print("Not prime")


# With function

def is_prime(f_num):
    f_stop = int(f_num ** 0.5)

    f_prime = True

    for f_i in range(2, f_stop):
        if f_num % f_i == 0:
            f_prime = False

    if f_prime:
        print("Prime")
    else:
        print("Not prime")


is_prime(num)
