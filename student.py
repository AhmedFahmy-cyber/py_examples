a=b=c=d=0
while True:
    
    num=int(input('Please enter grades:'))
    if num>=90 and num<=100:
        a+=1
    elif num>=80 and num<90:
        b+=1
    elif num>=60 and num<80:
        c+=1
    elif num>=0 and num<60:
        d+=1
    else:
        print('Out of range, please re-enter:')
        continue
    print(num)
    str1=int(input('Do you want to continue? 1/0:'))
    print(str1)
    if str1==0:
        break
print('>=90:',a)
print('>=80:',b)
print('>=60:',c)
print('<60:',d)
