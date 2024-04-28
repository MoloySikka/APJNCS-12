# 1 : id defined at local, enclosing, global and builtin levels.
print("\n1 : id defined at local, enclosing, global and builtin levels.\n")
id = 25

print(f"Global: {id}")


def outer():
    id = 25
    print(f"Enclosing: {id}")

    def inner():
        id = 45
        print(f"Local: {id}")

    inner()
    print(f"Enclosing: {id}")


outer()
print(f"Global: {id}")
del id

# 2 : id defined at enclosing, global and builtin levels.
print("\n2 : id defined at enclosing, global and builtin levels.\n")
id = 25

print(f"Global: {id}")


def outer():
    id = 25
    print(f"Enclosing: {id}")

    def inner():
        # id = 45
        print(f"Local: {id}")

    inner()
    print(f"Enclosing: {id}")


outer()
print(f"Global: {id}")
del id

# 3 : id defined at global and builtin levels.
print("\n3 : id defined at global and builtin levels.\n")
id = 25

print(f"Global: {id}")


def outer():
    # id = 25
    print(f"Enclosing: {id}")

    def inner():
        # id = 45
        print(f"Local: {id}")

    inner()
    print(f"Enclosing: {id}")


outer()
print(f"Global: {id}")
del id

# 4 : id defined at builtin level.
print("\n4 : id defined at builtin level.\n")
# id = 25

print(f"Global: {id}")


def outer():
    # id = 25
    print(f"Enclosing: {id}")

    def inner():
        # id = 45
        print(f"Local: {id}")

    inner()
    print(f"Enclosing: {id}")


outer()
print(f"Global: {id}")
