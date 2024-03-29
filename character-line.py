char = input("Enter the character you want to make the line with: ")
length = int(input("Enter length of the line: "))

# without function
print(char * length)

# with function
def character_line(char, length):
  print(char * length)

print()
character_line(char, length)
