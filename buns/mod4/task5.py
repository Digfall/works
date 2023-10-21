def count_letters(filename):
    char_count = {}
    
    # Открываем файл для чтения
    with open(filename, 'r') as file:
        # Читаем содержимое файла построчно
        for line in file:
            # Удаляем символы перевода строки
            line = line.strip()
            
            # Подсчитываем количество каждого символа в строке
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    
    # Сортируем результат по частоте встречаемости букв
    sorted_count = sorted(char_count.items(), key=lambda x: x[1])
    
    return sorted_count

filename = "ввод.txt"
result = count_letters(filename)

# Открываем файл для записи
with open("вывод.txt", 'w') as file:
    # Записываем результат в файл
    for char, count in result:
        file.write(f"{char}: {count}\n")
