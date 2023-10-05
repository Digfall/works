a = int(input('Введите число: '))
if a <= 0:
    print("Неверный ввод")
else:
    two = bin(a)[2:]
    eight = oct(a)[2:]
    sixth = hex(a)[2:]
print(two,eight,sixth)

