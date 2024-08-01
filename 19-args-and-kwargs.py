# 23/4/24
# AIM: To demonstrate the usage of *args and **kwargs in user-defined Python functions.

def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


def describe_movie(**kwargs):
    description = ""
    for key, value in kwargs.items():
        description += f"{key.capitalize()}: {value}\n"
    return description


# Example usage
total_product = product(2, 3, 4)
print("Product of numbers:", total_product)
print()

movie_description = describe_movie(title="Inception", director="Christopher Nolan", year=2010, genre="Science Fiction")
print("Movie description:\n", movie_description, sep="")
