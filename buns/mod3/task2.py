number = int(input("Число:\n"))
if number > 0: print(f"В 2-ой: {bin(number)[2:]}\nВ 8-ой: {oct(number)[2:]}\nВ 16-ой: {hex(number)[2:]}")
else: print("Неверный ввод")
