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
def box(character, length, height):
  print(character * length)

  for _ in range(height - 2):
    print(character, end='')
    print(" " * (length - 2), end='')
    print(character)

  print(character * length)

box(character, length, height)
