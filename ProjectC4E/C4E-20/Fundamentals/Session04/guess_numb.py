input('Enter')
print('''
All you have to do is to answer to my guess
'c' if 'c'orrect
's' if 's'maller
'l' if 'l'arger
''')
low = 0
high = 100
conf = True
while conf:
    mid = (high + low)//2
    ans = input('Is {} your number?'.format(mid))
    if ans == 's':
        low = mid
    elif ans == 'l':
        high = mid
    elif ans == 'c':
        conf = False
        
        



