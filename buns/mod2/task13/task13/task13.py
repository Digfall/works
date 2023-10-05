a = input()
even = 0
odd = 0
lora = True
while 1:
    if len(a)!= 0:
        s = a[0]
        a = a[1::]
        if lora:
            odd += int(s)
            lora = False
        else:
            even += int(s)
            lora = True
    else:break
if (3 * even + odd) %10 == 0:print('yes')
else:print('no')
