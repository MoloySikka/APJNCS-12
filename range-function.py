# Without function

r_start = int(input("Enter 'start' value: "))
r_stop = int(input("Enter 'stop' value: "))
r_step = int(input("Enter 'step' value: "))

range_list = []

i = 1

while i < r_stop:
    range_list.append(i)
    i += r_step

print()

# With function
def my_range(start=0, stop=0, step=1):
    if start != 0 and stop == 0 and step == 1:
        stop = start
        start = 0

    f_range_list = []

    f_i = start
    while f_i < stop:
        f_range_list.append(f_i)
        f_i += step

    return f_range_list


r_start = int(input("Enter 'start' value: "))
r_stop = int(input("Enter 'stop' value: "))
r_step = int(input("Enter 'step' value: "))


print(my_range(r_start, r_stop, r_step))
