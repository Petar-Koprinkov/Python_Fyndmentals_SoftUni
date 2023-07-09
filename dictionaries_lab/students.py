message = input()
dictionary = {}

while ":" in message:
    student_name, student_id, student_course = message.split(":")

    if student_course not in dictionary.keys():
        dictionary[student_course] = {student_id: student_name}
    else:
        dictionary[student_course][student_id] = student_name

    message = input()

message = message.replace("_", " ")

for key, value in dictionary[message].items():
    print(f"{value} - {key}")

