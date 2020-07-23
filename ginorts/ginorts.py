s = input()
l = [[],[],[],[]]
for i in s:
    if i.isdigit():
        if int(i) % 2 == 0:
            l[3].append(i)
        else:
            l[2].append(i)
    elif i.isupper():
        l[1].append(i)
    else:
        l[0].append(i)
newS = ''
for i in range(len(l)):
    l[i].sort()
    newS += ''.join(l[i])
print(newS)
