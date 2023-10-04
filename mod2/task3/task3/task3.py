a = int(input())
b = int(input())
if a > b:
    a, b = b, a
c = int(input())
if b > c:
    b, c = c, b
    if a > b:
        a, b = b, a
print (b)
