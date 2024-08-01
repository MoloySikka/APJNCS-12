# 19/3/24
# AIM: WAP to create a line with a given character

char = input("Enter the character you want to make the line with: ")
length = int(input("Enter length of the line: "))

# without function
print(char * length)


# with function
def character_line(f_char, f_length):
    print(f_char * f_length)


print()
character_line(char, length)
