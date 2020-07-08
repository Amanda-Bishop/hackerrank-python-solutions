def print_rangoli(size):
    s = []
    w = (size * 2) - 1 + (size * 2) - 2
    lines = []
    for i in range(size,0,-1):
        s += chr(i + 96)
        if i == size:
            newS = ''.join(s)
        else:
            newS = '-'.join(s)
            if i == (size - 1):
                newS +=  '-' + s[0]
            else:
                newS += '-' + '-'.join(s[-2:0:-1]) + '-' + s[0]
        print(newS.center(w,'-'))
        lines = [newS] + lines

    for i in range(1, len(lines)):
        print(lines[i].center(w,'-'))

print_rangoli(int(input()))
