
'''docstring: This is a simple program that takes a list of student grades and'''

def student_grades(grades, names):
    '''This function takes a list of student grades and returns the grades after'''
    for i in range(len(grades)-1):
        grades[i] -=5

    for i, grade in enumerate(grades):
        grade -=5
        if grade <50:
            grade += 10
            print(f"Student {i} has failed with grade {grade}")
        else:
            print(f"Student {i} has passed with grade {grade}")

    for name in names:
        name += " is a student"

    return grades, names


students_grades = [91, 88, 75, 95, 80, 85,23, 100, 10, 11,76, 54, 32, 65, 43, 76,
          87, 98, 99,45, 67, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
std_names =["Joe", "Jane", "John", "Jack", "Jill"]

# print(student_grades(students_grades, std_names))

print(students_grades[0], std_names[0])
