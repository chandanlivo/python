x = int(input('Enter the value of x:\n'))

match x:
    case 0:
        print('The x is zero')

    case 4:
        print('case is 4')

    case _:
        print(x)        