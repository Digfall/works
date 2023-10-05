site = input("Введите домен: ")
word = ''
for x in site:
    if x == '.':
        print(word)
        word = ''
    else:
        word += x
print(word)
