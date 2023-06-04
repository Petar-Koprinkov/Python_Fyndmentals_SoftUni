def loading_bar(some_number):
    if some_number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    loaded_percentage = some_number // 10
    not_loaded_percentage = 10 - loaded_percentage
    return f"{some_number}% [{'%' * loaded_percentage}{'.' * not_loaded_percentage}]\nStill loading..."


number = int(input())
print(loading_bar(number))