import re
for i in range(int(input())):
    validNums = '456'
    r = '[0123456789]*[0123456789]+[0123456789]+[0123456789]'
    groupsOf4 = True
    cc = input().split('-')
    num = ''.join(cc)
    if len(cc) > 1 and any(len(j) != 4 for j in cc):
        groupsOf4 = False
    repeats = re.search(r'(\d)\1{3}',num)
    if num[0] in validNums and len(num) == 16 and num.isdigit() and groupsOf4 and repeats == None: 
        print('Valid')
    else:
        print('Invalid')
