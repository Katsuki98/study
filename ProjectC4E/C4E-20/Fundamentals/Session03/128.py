numb = [1,4,1,64,2,128,5,4,7,31]
print('Trong dãy số: ')
print(*numb,sep=', ')
for i in range(len(numb)):
    if i < len(numb) - 1:
        for j in range(len(numb)):
            if i + j + 1 <= len(numb) - 1:
                total = int(numb[i]) * int(numb[i + j + 1])
                if total == 128:
                    print('{} và {} tại vị trí {} và {}'.format(numb[i],numb[i + j + 1], i + 1, i + j + 2))
                else:
                    j = j + 1
