while True:
    
    n1 = input('Enter Number 1 : ')
    n2 = input('Enter Number 2 : ')
    if  n1 == 'x':
         print('thanks....')
         break
    n1 = int(n1)
    n2 = int(n2)
    if n1 < n2:
        
        #n1 = int(n1)
        for x in range(n1+1,n2):    
            print(x)
    else:
            
        print('n1 must be less than n2 ')



        

                
            
