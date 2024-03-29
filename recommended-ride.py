# Without function
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age!")
elif age <= 3:
    print("You're too young!")
elif age <= 10:
    print("Try the Carrousel!")
elif age <= 15:
    print("Try the Ride of Doom!")
elif age <= 18:
    print("Try the Cranium Shaker!")
else:
    print("Try the Not-So-Safe-Coaster  (adult content)!")


# With function
def age_recommend(age):
    if age < 0:
        print("Invalid age!")
    elif age <= 3:
        print("You're too young!")
    elif age <= 10:
        print("Try the Carrousel!")
    elif age <= 15:
        print("Try the Ride of Doom!")
    elif age <= 18:
        print("Try the Cranium Shaker!")
    else:
        print("Try the Not-So-Safe-Coaster  (adult content)!")


age_recommend(age)
