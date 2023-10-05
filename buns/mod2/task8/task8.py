site, i = map(str, input().split(','))
count = 0
for x in site:
    if x == i:
        count += 1
    else:
        break
print(count)
