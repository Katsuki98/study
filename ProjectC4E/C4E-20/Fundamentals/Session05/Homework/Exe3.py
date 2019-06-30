bac = int(input('How many B bacterias are there? '))
time = int(input('How much time in minutes will we wait? '))
n = 2 ** (time // 2)
print('After ',time,' minutes, we would have ',bac * n,' bacterias')