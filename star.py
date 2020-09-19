for r in range(9):
    if r <5 :
        for x in range(r+1):
            print('*',end='')

    else:
         for x in range(9-r):
             print('*',end='')

    print()

print('*' * 20)   
