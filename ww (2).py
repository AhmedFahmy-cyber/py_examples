rows=int(input('enter :'))
s=rows//2+1
x=rows-s
for i in range(s):
    for j in range(s-1,i,-1):
        print(' ',end='')
    for k in range(i*2+1):
        print('*',end='')
    print()
for i in range(1,x+1):
    for j in range(i):
        print('    ',end='')
    for k in range((s-i)*2-1):
        print('*',end='')
    print()
