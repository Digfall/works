cifri = input().replace(" ", "")
boo = False
for x in range(len(cifri)-1):
    for i in range(x+1, len(cifri)):
        if cifri[x] == cifri[i]:
            boo = True
        break
print(boo) 
