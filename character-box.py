character = input("Enter character with which you want to make the box: ")
height = int(input("Enter height of box: "))
length = int(input("Enter length of box: "))

# without function

print(character * length)

for _ in range(height - 2):
    print(character, end='')
    print(" " * (length - 2), end='')
    print(character)

print(character * length)


# with function
def box(f_character, f_length, f_height):
    print(f_character * f_length)

    for _ in range(f_height - 2):
        print(f_character, end='')
        print(" " * (f_length - 2), end='')
        print(f_character)

    print(f_character * f_length)


box(character, length, height)
