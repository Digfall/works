def can_form_palindrome(word):
    char_count = {}
    
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    
    palindrome = ""
    middle_char = ""
    
    for char, count in char_count.items():
        if count % 2 == 0:
            palindrome += char * (count // 2)
        else:
            middle_char = char
    
    palindrome += middle_char
    
    palindrome += palindrome[::-1]
    
    return palindrome

word = "шалаш"
result = can_form_palindrome(word)
print(result)
