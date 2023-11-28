grades_dict = {}
with open("input3.txt", "r") as file:
    for line in file:
        data = line.strip().split()
        student_name = data[0]
        grade = int(data[1])
        grades_dict[student_name] = grade
def average_grade(grades):
    total_grades = sum(grades.values())
    num_students = len(grades)
    return total_grades / num_students

avg = average_grade(grades_dict)
print(f"Средний балл по всем студентам: {avg}")
def filter_grades(grades, threshold):
    filtered_grades = {name: grade for name, grade in grades.items() if grade > threshold}
    return filtered_grades

threshold = 80
filtered_dict = filter_grades(grades_dict, threshold)
print(f"Студенты с оценкой выше {threshold}: {filtered_dict}")