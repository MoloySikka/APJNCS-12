# 19/3/24
# AIM: WAP to give a student their grade after they enter their marks

marks = int(input("Enter the student's marks (0-100): "))

# Without function
if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
else:
    if marks >= 90:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 33:
        grade = "D"
    else:
        grade = "F"

    print(f"The student's grade is: {grade}")

# With function
def get_grade(f_marks):
    if f_marks >= 90:
        return "A"
    elif f_marks >= 70:
        return "B"
    elif f_marks >= 50:
        return "C"
    elif f_marks >= 33:
        return "D"
    else:
        return "F"


print(f"The student's grade is: {get_grade(marks)}")
