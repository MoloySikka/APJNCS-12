# 24/04/2024
# AIM: WAP to handle the various errors using try and except blocks.

try:
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    c = a / b
    print(c)

except ValueError:
    print("Wrong input. Enter an integer instead.")

except TypeError:
    print("Wrong input. Can't operate string.")

except ZeroDivisionError:
    print("Enter a correct value for b. It can't be 0.")

except Exception as e:
    print("The respective error is", e)

else:
    print("The code has no errors.")

finally:
    print("The code has been executed.")
