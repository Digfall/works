sentence = input().replace(" ", "")
count = 0
count1 = 0
for x in sentence:
    if x in ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]:
        count += 1
    else:
        count1 += 1

print(f"В данном нечте {count} глассных и {count1} согласных")
