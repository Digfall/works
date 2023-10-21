def fast_power(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        half_power = fast_power(base, exp // 2)
        return half_power * half_power
    else:
        return base * fast_power(base, exp - 1)

base = 2
exp = 10
result = fast_power(base, exp)
print(result)
