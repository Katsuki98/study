for i in range(5):
    
    for j in range(i):
    # mac dinh lan dau la 0 nen dong dau se ko co *    
        print('*', end='')
    print()

for i in range(10):

    for j in range(10):
        if j<=10 - i - 1:
            print('  ',end='')
        else:
            print('* ', end='')

    
    print()