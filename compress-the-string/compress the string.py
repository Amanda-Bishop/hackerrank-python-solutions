l = []
s = input()
for i in range(len(s)):
    if i != 0 and s[i-1] == s[i]:
        l[-1] = (l[-1][0]+1, int(s[i]))
    else:
        l.append((1,int(s[i])))
print(*l)
