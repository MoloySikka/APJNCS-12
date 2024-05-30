# Incomplete

import pickle

MENU_PROMPT = """

Inventory Manager
1) Create files: Master and Transactions
2) Add items.
3) Inventory report.
4) Update item master.
5) Delete from item master.
6) Purchase items.
7) Sales report.
0) Exit
Enter your choice:
"""


def create_files():
    with open('items.dat', 'wb') as _:
        pass
    with open('sales.dat', 'wb') as _:
        pass


def add_items():
    codes = []
    data = []

    with open('items.dat', 'rb') as f:
        while True:
            try:
                rec = pickle.load(f)
                codes.append(rec)
            except EOFError:
                break

    more = 'y'

    while more.lower() == 'y':
        while True:
            code = input('Enter item code (4 character alphanumeric)')
            if code in codes:
                print("That code already exists!")
            elif len(code) != 4 or not code.isalnum():
                print('Invalid code!')
            else:
                break

        desc = input('Enter item description (max. 20 characters): ')
        desc = desc[:20]
        price = float(input('Enter selling price: '))
        disc = float(input('Enter discount percent: '))
        qty = float(input('Enter balance quantity: '))
        re_level = float(input('Enter reorder level: '))
        re_qty = float(input('Enter reorder quantity: '))

        rec = [code, desc, price, disc, qty, re_level, re_qty]

        data.append(rec)

        more = input('More data?m (y/n): ')

        with open('items.dat', 'ab') as f:
            for rec in data:
                pickle.dump(rec, f)


def menu():
    """Main menu driver"""
    while True:
        while True:
            try:
                ch = int(input(MENU_PROMPT))
            except ValueError:
                print("Invalid!")
            else:
                break

        if ch == 1:
            pass

        elif ch == 2:
            pass

        elif ch == 3:
            pass

        elif ch == 4:
            pass

        elif ch == 5:
            pass

        elif ch == 6:
            pass

        elif ch == 7:
            pass

        elif ch == 0:
            print("Thank you for using my program!")
            return

        else:
            print("Invalid!")
