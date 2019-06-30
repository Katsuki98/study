num = int(input('Enter a number: '))
# for i in range(2,num):
#     if num % i == 0:
#         print(num ,'is not a prime') 
#         break
#     else:
#         print(num, 'is a prime')
#         break

i = 2
prime = True

while i < num:
    if num % i == 0:
        prime = False
    i += 1

if prime:
    print('{} is a prime number'.format(num))
else:
    print('{} is not a prime number'.format(num))
         