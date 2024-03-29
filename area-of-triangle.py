a = int(input("Enter length of first side: "))
b = int(input("Enter length of second side: "))
c = int(input("Enter length of third side: "))

# Without function

s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Area is {:.2f} sq. units".format(area))


# With function

def area_of_triangle(a, b, c):
    s = (a + b + c)/2

    area = (s*(s-a)*(s-b)*(s-c))**0.5

    print("Area is {:.2f} sq. units".format(area))

area_of_triangle(a, b, c)
