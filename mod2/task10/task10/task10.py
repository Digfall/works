sentence = input()
word = ""
for char in range(1, len(sentence)):
    if sentence[char] == " ":
        word += sentence[char-1]

print(word + sentence[len(sentence)-1])
