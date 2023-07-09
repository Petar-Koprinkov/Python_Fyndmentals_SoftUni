def add_user(current_dictionary, current_course_name, current_student_name):
    if current_course_name not in current_dictionary.keys():
        dictionary[current_course_name] = []
    dictionary[current_course_name].append(current_student_name)

    return dictionary


command = input()
dictionary = {}

while command != "end":

    command = command.split(" : ")
    course_name, student_name = command
    dictionary = add_user(dictionary, course_name, student_name)

    command = input()

for key, value in dictionary.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")









