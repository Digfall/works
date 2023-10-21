def check_numbers(numbers):
    if len(set(numbers)) == 1:
        return "Все числа равны"
    elif len(set(numbers)) == len(numbers):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"

numbers = [1, 2, 3, 2, 4]
result = check_numbers(numbers)
print(result)
