num = int(input("Enter number: "))
n = int(input("Enter no. of multiples: "))

# Without function
for i in range(1, n + 1):
  print(f"{num} × {i} = {num * i}")

# With function
def table(num, n):
  for i in range(1, n + 1):
    print(f"{num} × {i} = {num * i}")

print()

table(num, n)