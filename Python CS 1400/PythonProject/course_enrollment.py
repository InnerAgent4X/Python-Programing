import sys



def print_student_info(student_IDs, students):
    print("Student ID search")
    while True:
        try:
            ID_search = (f"S{input("Please enter student ID as three numbers eg. 123: ")}")
            if ID_search in student_IDs:
                student_data = students.get(ID_search)
                print("Student ID: ", ID_search)
                print("Student Name: ", student_data["name"])
                print("Major: ", student_data["major"])
                print("Courses: ", student_data["courses"])
                break
            else:
                print("Student not found! Please try a different ID.")
        except ValueError:
            print("Invalid Format!")

def enroll_student(student_ID, students):
    print("not done yet")









def main():
    students = {
        "S001": {"name": "Alice", "major": "CS", "courses": ["ENGL1010", "MATH1035"]},
        "S002": {"name": "Bob", "major": "IS", "courses": ["INFO2410", "CS1400"]},
        "S003": {"name": "Charlie", "major": "DS", "courses": ["CS1400", "MATH1035"]}

    }

    student_IDs = list(students.keys())

    print_student_info(student_IDs, students)



if __name__ == '__main__':
    main()