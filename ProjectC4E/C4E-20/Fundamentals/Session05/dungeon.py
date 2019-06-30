map = {
    'size_x': 4,
    'size_y': 4,
}

player = {
    'x': 1,
    'y': 2,
}

exit = {
    'x': 3,
    'y': 2,
}

key = {
    'x': 2,
    'y': 1,
}

playing = True

while playing:
    for y in range(map['size_y']):
        for x in range(map['size_x']):

            player_is_here = False
            if y == player['y'] and x == player['x']:
                player_is_here = True

            exit_is_here = False
            if y == exit['y'] and x == exit['x']:
                exit_is_here = True

            key_is_here = False
            if y == key['y'] and x == key['x']:
                key_is_here = True

            if player_is_here:
                print('P ',end='')
            elif exit_is_here:
                print('E ',end='')
            elif key_is_here:
                print('K ',end='')
            else:
                print('- ',end='')
        print()

    
    
    if player == exit and player != key:
        print("You can't exit, please acquire the key first")
    if player != exit:
        if player != key:
            cond = False
        else:
            print("You've just picked up a key!!!")
            key = player
            cond = False
    elif player == exit and player == key:
        print("Congrats, you've just escaped the dungeon")
        break

    move = input('Your move: ').upper()
    dx = 0
    dy = 0
    if move == 'W':
        dy = -1
    elif move == 'A':
        dx = -1
    elif move == 'S':
        dy = 1
    elif move == 'D':
        dx = 1
    else:
        playing = False

    if player != key and player['x'] + dx == exit['x'] and player['y'] == exit['y']:
        if dx == 1 or dx == -1:
            dx = 0
            print("You can't exit, please acquire the key first")
    if player != key and player['x'] == exit['x'] and player['y'] + dy == exit['y']:
        if dy == 1 or dy == -1:
            dy = 0
            print("You can't exit, please acquire the key first")

    if 0 <= player['x'] + dx < map['size_x'] and \
        0 <= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy
    
   

