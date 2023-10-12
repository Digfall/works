a, b, c = map(int, input("Числа:\n").split(" "))
center = a + b + c - max(a, b, c) - min(a, b, c)
print(center)