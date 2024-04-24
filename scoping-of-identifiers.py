# 1 : id defined at local, enclosing, global and builtin levels.
print("\n1 : id defined at local, enclosing, global and builtin levels.\n")
id = 25

print(f"Global: {id}")


def outer_1():
    id = 25
    print(f"Enclosing: {id}")

    def inner_1():
        id = 45
        print(f"Local: {id}")

    inner_1()
    print(f"Enclosing: {id}")


outer_1()
print(f"Global: {id}")
del id

# 2 : id defined at enclosing, global and builtin levels.
print("\n2 : id defined at enclosing, global and builtin levels.\n")
id = 25

print(f"Global: {id}")


def outer_1():
    id = 25
    print(f"Enclosing: {id}")

    def inner_1():
        # id = 45
        print(f"Local: {id}")

    inner_1()
    print(f"Enclosing: {id}")


outer_1()
print(f"Global: {id}")
del id

# 3 : id defined at global and builtin levels.
print("\n3 : id defined at global and builtin levels.\n")
id = 25

print(f"Global: {id}")


def outer_1():
    # id = 25
    print(f"Enclosing: {id}")

    def inner_1():
        # id = 45
        print(f"Local: {id}")

    inner_1()
    print(f"Enclosing: {id}")


outer_1()
print(f"Global: {id}")
del id

# 4 : id defined at builtin level.
print("\n4 : id defined at builtin level.\n")
# id = 25

print(f"Global: {id}")


def outer_1():
    # id = 25
    print(f"Enclosing: {id}")

    def inner_1():
        # id = 45
        print(f"Local: {id}")

    inner_1()
    print(f"Enclosing: {id}")


outer_1()
print(f"Global: {id}")
