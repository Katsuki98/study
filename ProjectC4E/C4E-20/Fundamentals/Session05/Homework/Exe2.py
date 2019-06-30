numbers = [2,7,1,2,1,9,7,1]
print(numbers)
num = int(input('Enter a number: '))
a = 0
i = 0
while i <= len(numbers) - 1:
    if num == numbers[i]:
        a += 1
        i += 1
    else:
        i += 1

print(num,' appears ',a,' in my list')
            
       

