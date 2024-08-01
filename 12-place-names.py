# 1/4/24
# AIM: WAP to take place names from a given dictionary and print names which have more than 5 letters converted to uppercase

# Without function

PLACES = {
    1: "Delhi",
    2: "London",
    3: "Paris",
    4: "New York",
    5: "Doha",
}
for place in PLACES.values():
    if len(place) > 5:
        print(place.upper())

# With function

def place_names(places):
    for place in places.values():
        if len(place) > 5:
            print(place.upper())

place_names(PLACES)
