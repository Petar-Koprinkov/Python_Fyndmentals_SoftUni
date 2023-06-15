first_employee_efficiency_per_hour = int(input())
second_employee_efficiency_per_hour = int(input())
third_employee_efficiency_per_hour = int(input())
student_count = int(input())
total_efficiency = first_employee_efficiency_per_hour + \
                   second_employee_efficiency_per_hour + \
                   third_employee_efficiency_per_hour
time_needed = 0
time_counter = 0

while student_count > 0:
    time_counter += 1
    time_needed += 1

    if time_counter % 4 != 0:
        student_count -= total_efficiency
    else:
        continue

print(f"Time needed: {time_needed}h.")

