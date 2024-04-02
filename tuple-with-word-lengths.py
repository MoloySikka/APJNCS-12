# 1/4/24

# Without function

string = "Come let us have some fun"

lst = string.split()

tup = ()

for word in lst:
    tup += len(word),

print(tup)

# With function

def word_lengths(f_string):
    lst = f_string.split()

    tup = ()

    for word in lst:
        tup += len(word),

    return tup

print(word_lengths(string))
    
    
