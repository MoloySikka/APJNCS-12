# 19/3/24
a = int(input("Enter length of first side: "))
b = int(input("Enter length of second side: "))
c = int(input("Enter length of third side: "))

# Without function

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("Area is {:.2f} sq. units".format(area))


# With function

def area_of_triangle(f_a, f_b, f_c):
    f_s = (f_a + f_b + f_c) / 2

    f_area = (f_s * (f_s - f_a) * (f_s - f_b) * (f_s - f_c)) ** 0.5

    print("Area is {:.2f} sq. units".format(f_area))


area_of_triangle(a, b, c)
