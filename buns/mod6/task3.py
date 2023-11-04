def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return num == total

def get_armstrong_numbers():
    num = 10
    while True:
        if is_armstrong_number(num):
            yield num
        num += 1

# Вывод чисел Армстронга
for i, armstrong in enumerate(get_armstrong_numbers()):
    if i >= 8:
        break
    print(armstrong, end=' ')
