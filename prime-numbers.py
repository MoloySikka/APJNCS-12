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

def is_prime(num):
    stop = int(num ** 0.5)

    prime = True

    for i in range(2, stop):
        if num % i == 0:
            prime = False

    if prime:
        print("Prime")
    else:
        print("Not prime")


is_prime(num)
