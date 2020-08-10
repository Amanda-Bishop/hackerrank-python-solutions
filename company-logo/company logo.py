s = input()
ltrs = {}
for i in range(len(s)):
    if i == 0 or s[i] not in ltrs:
        ltrs[s[i]] = 1
    else:
        ltrs[s[i]] += 1
mostLtrs = sorted(ltrs, key=ltrs.get, reverse=True)
maxv = 0
count = {}
for i in range(len(mostLtrs)):
    if i == 0 or ltrs[mostLtrs[i]] not in count:
        if i > 2 and ltrs[mostLtrs[i]] not in count:
            break
        maxv = ltrs[mostLtrs[i]]
        count[maxv] = 1
            
    else:
        count[maxv] += 1
            
values = list(count.values())
keys = list(count.keys())
most = []

for i in range(len(values)):
    if values[i] == 1: 
        num = sum(values[:i])
        most.append([mostLtrs[num],keys[i]])
    
    else:
        if i == 0:
            n = values[i]
            temp = mostLtrs[i:values[i]]
        else:
            n = 3-len(most)
            temp = mostLtrs[i:values[i]+1]
        temp.sort()
        for j in range(n):
            most.append([temp[j],keys[i]])
for i in most[:3]:
    print(i[0],i[1])
