def add_grade(current_dictionary, current_number):
    for i in range(current_number):
        name = input()
        grade = float(input())

        if name not in current_dictionary.keys():
            current_dictionary[name] = []
        current_dictionary[name].append(grade)

    return current_dictionary


def average_number(current_dictionary):
    for key, value in current_dictionary.items():
        average_grade = sum(value) / len(value)
        dictionary[key] = average_grade
    return current_dictionary


number = int(input())
dictionary = {}

dictionary = add_grade(dictionary, number)
dictionary = average_number(dictionary)
for student_name, student_grade in dictionary.items():
    if student_grade >= 4.50:
        print(f"{student_name} -> {student_grade:.2f}")

