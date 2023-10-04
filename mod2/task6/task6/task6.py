site = input()
word = ''
for x in site:
    if x == '.':
        print(word)
        word = ''
    else:
        word += x
print(word)
