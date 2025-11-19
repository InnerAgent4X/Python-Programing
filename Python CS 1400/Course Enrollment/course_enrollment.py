import sys



def print_student_info(student_IDs, students):
    print("Student ID search")
    while True:
        try:
            ID_search = f"S{input("Please enter student ID as three numbers eg. 123 or Q to return: ")}"
            #Checks to see if the ID is valid(contained in the dictionary)
            if ID_search in student_IDs:
                student_data = students.get(ID_search)
                print("Student ID: ", ID_search)
                print("Student Name: ", student_data["name"])
                print("Major: ", student_data["major"])
                print("Courses: ", student_data["courses"])
                break
            elif ID_search == "SQ" or ID_search == "Sq":
                break
            else:
                print("Student not found! Please try a different ID.")
        except ValueError:
            print("Invalid Format!")

def enroll_student(student_IDs, students):
    while True:
        try:
            ID_search = f"S{input("Please enter student ID as three numbers eg. 123: ")}"
            if ID_search in student_IDs:
                student_data = students.get(ID_search)
                course_add = input("Enter course to enroll: ")
                #validates that the course is new
                if course_add not in student_data["courses"]:
                    student_data["courses"].append(course_add)
                    print(f"Enrolled {student_data['name']} in {course_add}")
                    break
                else:
                    print("Student already enrolled in this course!")
            else:
                print("Student not found! Please try a different ID.")
        except ValueError:
            print("Invalid Format!")


def drop_students(student_IDs, students):
    while True:
        try:
            drop_command = f"S{input("Please enter student ID as three numbers eg. 123: ")}"
            if drop_command in student_IDs:
                student_data = students.get(drop_command)
                print(f"Dropped student {drop_command}, {student_data["name"]}")
                students.pop(drop_command)
                break
            else:
                print("Student not found! Please try a different ID.")
        except ValueError:
            print("Invalid Format!")



def main():
    students = {
        "S001": {"name": "Alice", "major": "CS", "courses": ["ENGL1010", "MATH1035"]},
        "S002": {"name": "Bob", "major": "IS", "courses": ["INFO2410", "CS1400"]},
        "S003": {"name": "Charlie", "major": "DS", "courses": ["CS1400", "MATH1035"]}

    }
    #creates a list of all the first keys(the student IDs
    student_IDs = list(students.keys())
    print("Welcome to the course enrollment program!")
    print(f"Here are all the current student IDs: {student_IDs}")

    while True:
        print("What would you like to do? View student info? Enroll students into courses? Drop students from database? Quit program?")
        try:
            command = input("Please enter V, E, D, or Q: ")
            command = command.upper()
            if command == "V":
                print_student_info(student_IDs, students)
            elif command == "E":
                enroll_student(student_IDs, students)
            elif command == "D":
                drop_students(student_IDs, students)
            elif command == "Q":
                break
        except ValueError:
            print("Invalid Command, Please enter V, E, or D.")

    print("Summery")
    print("=" * 20)
    for student, info in students.items():
        print(f"Student ID: {student}")
        print(f"Student Name: {info["name"]}")
        print(f"Major: {info["major"]}")
        print(f"Courses: {info["courses"]}")
        print("=" * 20)

    sys.exit()



if __name__ == '__main__':
    main()