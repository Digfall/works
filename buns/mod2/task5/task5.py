def alphabet(i, n):
    value = ord(i)
    moved_value = value + n
    char = chr(moved_value)
    return char
i = input("Введите символ латинского алфавита: ")
n = int(input("Введите целое число: "))
result = alphabet(i, n)
print( result)

