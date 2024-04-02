lst = eval(input("Enter a list: "))
lis = lst.copy()

for i in range(len(lst)):
    if lst[i] % 2:
        lst[i] -= 1
    else:
        lst[i] += 2

print(lst)

# With functions
def modify_list(l):
    for i in range(len(l)):
        if l[i] % 2:
            l[i] -= 1
        else:
            l[i] += 2

    return l

print(modify_list(lis))
