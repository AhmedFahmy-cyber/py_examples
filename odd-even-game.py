print('welcome to the game')
print('Enter number to check even or odd')
print('Enter X to exit the game')

while True:
    
    number = input('Enter number here:')
    if number == 'x':
        print('closing the game')
        print('thanks ...')
        break
    try:
        number = int(number)
        if number % 2 == 0 :
            print('Even number')
           
        else:
            print('Odd number')
    except ValueError:
        print('please enter valid numer') 


