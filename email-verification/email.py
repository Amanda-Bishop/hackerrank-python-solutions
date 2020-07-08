import re
for i in range(int(input())):
    l = input().split()
    email = l[1][1:-1].split('@')
    user = re.split('[-._]', email[0])
    try:
        domain = email[1].split('.')
    except:
        domain = None
    if len(email) == 2 and ''.join(user).isalnum() and email[0][0].isalpha() and len(domain) == 2 and domain[0].isalpha() and domain[1].isalpha() and len(domain[1]) > 0 and len(domain[1]) < 4:
        print(' '.join(l))
