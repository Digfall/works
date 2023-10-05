cifri = input('Введите число: ')
count1 = 0
count0 = 0
for x in cifri:
        if x == '1':
            count1 += 1
        elif x == '0':
            count0 += 1
            
if count0 == count1:
     print("yes")
else:
     print("no")
