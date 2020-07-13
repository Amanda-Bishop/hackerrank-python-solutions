x = []
for i in range(int(input.split()[1])):
    x += [list(map(float, input().split()))]
s = zip(*x)
for i in s:
    print(sum(list(i))/len(list(i)))
