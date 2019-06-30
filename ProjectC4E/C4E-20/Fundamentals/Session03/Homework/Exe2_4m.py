sizes = [50, 9, 240, 105, 4]
print('Hello, my name is Son and these are my sheep sizes')
print(sizes)
print()

for i in range(4):
    print('MONTH', i + 1)
    for i in range(len(sizes)):
        sizes[i] += 50
    print('One month passed, now here is my flock')
    print(sizes)
    max = 0
    for i in range(len(sizes)):
        if sizes[i] > max:
            max = sizes[i]
            maxIndex = i
    print('Now my biggest sheep has size', max, "let's shear it")
    sizes[maxIndex] = 8
    print('After shearing, here is my flock')
    print(sizes)
    print()

#sell
total = sum(sizes)
money = total * 2
print('My flock has size in total: ', total)
print('I would get ', total, '* 2$ =', money,'$')