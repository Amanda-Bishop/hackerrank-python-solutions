from collections import OrderedDict
ordd = OrderedDict()

for i in range(int(input())):
    inp = input().split()
    name = ' '.join(inp[0:-1])
    if name not in ordd:
        ordd[name] = int(inp[-1])
    else:
        ordd[name] += int(inp[-1])

for i in ordd:
    print(i, str(ordd[i]))
