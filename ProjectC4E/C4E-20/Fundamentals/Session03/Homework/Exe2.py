#1
sizes = [50, 9, 240, 105, 4]
print('Hello, my name is Son and these are my sheep sizes')
print(sizes)
print()

#2
max = 0
for i in range(len(sizes)):
    if sizes[i] > max:
        max = sizes[i]
        maxIndex = i
print('Now my biggest sheep has size', max, "let's shear it")
print()

#3
sizes[maxIndex] = 8
print('After shearing, here is my flock')
print(sizes)
print()

#4
for j in range(len(sizes)):
    sizes[j] += 50
print('One month passed, now here is my flock')
print(sizes)

