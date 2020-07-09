h,w = list(map(int,input().split()))
s = '.|.'
increasing = True
first = False
for i in range(h):
    if i == (h // 2):
        print('WELCOME'.center(w,'-'))
        increasing = False
        first = True
    else:
        if i != 0:
            if increasing:
                s = s[:1] + '|..|..' + s[1:]
            else:
                if not first:
                    s = s[:1] + s[7:]
                first = False
        print(s.center(w,'-'))
