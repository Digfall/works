def euclid_alg(a, b):
    if b == 0:
        return a
    else:
        return euclid_alg(b, a % b)

a = 24
b = 36
result = euclid_alg(a, b)
print(result)
