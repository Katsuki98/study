from random import choice
words = ['champion','dungeon','vodka']
word = choice(words)
rand = list(word)
new = []

while len(rand) != 0:
    x = choice(rand)
    new.append(x)
    rand.remove(x)
print(*new)
guess = input('Enter a guess word: ')
if guess == word:
    print('Correct')
else:
    print('False')



