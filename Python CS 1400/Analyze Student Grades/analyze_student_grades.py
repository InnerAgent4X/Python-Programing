import sys

#Presents the values to work with as a list of tuples.
students = [("Alice", 87), ("Bob", 92), ("Charlie", 78), ("Dana", 85)]

#validates the input
for student in students:
    if type(student) == tuple and len(student) == 2:
        continue
    else:
        print("Invalid Student Info! Please enter info as a Tuple. eg. (name, grade)")
        sys.exit()

#Empty list to store all the scores
names = []
scores = []

def analyze_grades(students):

#makes the individual tuples accessible by calling them separately
    for student in students:
        name = student[0]
        grade = student[1]
        names.append(name)
        scores.append(grade)



def main():
    analyze_grades(students)

    #Gets the index number so that it can be used to match the name with the score
    max_index = scores.index(max(scores))
    min_index = scores.index(min(scores))

    print(f"Average: {round(sum(scores) / len(scores), 1)}")
    print(f"Highest grade: {scores[max_index]} ({names[max_index]})")
    print(f"Lowest grade: {scores[min_index]} ({names[min_index]})")





if __name__ == "__main__":
    main()