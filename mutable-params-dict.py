# 18/4/24
# AIM: WAP to demonstrate the mutability of a parameter when a dict is passed in.

def raise_marks(s, p):
    s['Marks'] = ((100 + p) / 100)
    s['Status'] = 'Changed'


S1 = {
    'R.no.': 1,
    'Name': 'Raj',
    'Marks': 75,
    'Status': '*'
}

S2 = {
    'R.no.': 3,
    'Name': 'Ken',
    'Marks': 60,
    'Status': '*'
}

raise_marks(S1, 5)
raise_marks(S2, 10)
print(S1)
print(S2)                   # Both dictionaries have been changed in place by the function
