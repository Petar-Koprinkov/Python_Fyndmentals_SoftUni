number_of_snowballs = int(input())
value = 0
max_weight = 0
max_time = 0
max_quality = 0

for snowball in range(1, number_of_snowballs + 1):
    weight_of_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = (weight_of_snowball / time_needed) ** quality

    if value < snowball_value:
        value = int(snowball_value)
        max_weight = weight_of_snowball
        max_time = time_needed
        max_quality = quality

print(f"{max_weight} : {max_time} = {value} ({max_quality})")

