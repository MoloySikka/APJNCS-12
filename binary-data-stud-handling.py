# 24/5/24
# AIM: To create a menu-driven student marks management system using binary file handling.
# Incomplete

import pickle

menu_prompt = """\nDo you want to:
1) Input student data.
2) View student data.
3) Search with roll no.
0) Exit
Enter your choice: """


def write_marks(marks_dict):
    try:

        with open("C:/Users/Admin/Desktop/students.dat", 'rb') as data:
            try:
                stud_data = pickle.load(data)
            except EOFError:
                stud_data = []

    except FileNotFoundError:
        stud_data = []

    stud_data.append(marks_dict)

    with open("C:/Users/Admin/Desktop/students.dat", 'wb') as data:
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
    print(f'| Roll no. |{'Name'.center(20)}| Marks |')
    print("-" * 41)
    with open("C:/Users/Admin/Desktop/students.dat", 'rb') as data:
        stud_data = pickle.load(data)
        for stud in stud_data:
            print(f'|{str(stud['R_no']).center(10)}|{stud['Name'].center(20)}|{str(stud['Marks']).center(7)}|')


def search_rno():
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
    tryr_no = 


def run():
    """Main menu driven program"""
    try:
        ch = int(input(menu_prompt))
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

    elif ch == 0:
        print("Thank you for using my program.")
        return

    else:
        print("Invalid")
        run()
        return


run()
