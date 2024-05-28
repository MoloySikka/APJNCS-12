# 24/5/24
# AIM: To create a menu-driven student marks management system using binary file handling.
# Incomplete

import pickle

MENU = """\nDo you want to:
1) Input student data.
2) View student data.
3) Search with roll no.
4) Update a record.
0) Exit.
Enter your choice: """

FILE = "C:/Users/Admin/Desktop/students.dat"


def write_marks(marks_dict):
    try:

        with open(FILE, 'rb') as data:
            try:
                stud_data = pickle.load(data)
            except EOFError:
                stud_data = []

    except FileNotFoundError:
        stud_data = []

    stud_data.append(marks_dict)

    with open(FILE, 'wb') as data:
        pickle.dump(stud_data, data)


def input_marks():
    """Takes data input and dumps to file."""
    while True:
        try:
            r_no = int(input('\nEnter roll number: '))
            break
        except ValueError:
            print('Invalid')

    name = input('Enter name: ')

    while True:
        try:
            marks = int(input('Enter marks: '))
            break
        except ValueError:
            print('Invalid')

    write_marks({"R_no": r_no, "Name": name, "Marks": marks})


def show_data():
    """Loads all data from file1"""
    print(f'\n| Roll no. |{'Name'.center(20)}| Marks |')
    print("-" * 41)
    try:
        with open(FILE, 'rb') as data:
            stud_data = pickle.load(data)
            for stud in stud_data:
                print(f'|{str(stud['R_no']).center(10)}|{stud['Name'].center(20)}|{str(stud['Marks']).center(7)}|')
    except FileNotFoundError:
        print("No data found!")


def search_rno():
    """Search for roll number and show corresponding record."""
    f = open('C:/Users/Admin/Desktop/students.dat', 'rb')
    flag = False
    print()
    r = int(input("Enter roll no to be searched: "))
    rec = pickle.load(f)
    for i in rec:
        if i['R_no'] == r:
            print()
            print('Roll No:', i['R_no'])
            print('Name:', i['Name'])
            print('Marks:', i['Marks'])
            flag = True
            break
    if not flag:
        print('No Records found')
    f.close()


def update_record():
    """Search for roll number and update corresponding record."""
    try:
        r_no = int(input('\nEnter the roll number for which the record has to be updated: '))
    except ValueError:
        print('Invalid!')
        update_record()
        return

    with open(FILE, 'rb') as data:
        stud_data = pickle.load(data)

    flag = False

    for stud in range(len(stud_data)):
        if stud_data[stud]['R_no'] == r_no:
            flag = True
            print()
            name = input('Enter changed name (leave empty for unchanged): ')
            marks = input('Enter changed marks (leave empty for unchanged): ')

            if not marks.isdigit() and marks:
                print('Invalid!')
                update_record()
                return

            if name:
                stud_data[stud]['Name'] = name

            if marks:
                stud_data[stud]['Marks'] = marks

            break

    if flag:

        with open(FILE, 'wb') as data:
            pickle.dump(stud_data, data)

        print(f'\nUpdated values: {str(stud_data[stud]['R_no']).center(10)}|{stud_data[stud]['Name'].center(20)}|'
              f'{str(stud_data[stud]['Marks']).center(7)}')

    else:
        print("That roll number was not found in the given data.")


def run():
    """Main menu driven program"""
    try:
        ch = int(input(MENU))
    except ValueError:
        print("Invalid")
        run()
        return

    if ch == 1:
        input_marks()
        run()
        return

    elif ch == 2:
        show_data()
        run()
        return

    elif ch == 3:
        search_rno()
        run()
        return

    elif ch == 4:
        update_record()
        run()
        return

    elif ch == 0:
        print("Thank you for using my program.")
        return

    else:
        print("Invalid")
        run()
        return


run()
