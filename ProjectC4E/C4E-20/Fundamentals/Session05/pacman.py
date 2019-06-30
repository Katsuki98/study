from random import choice
map = {
    'size_x': 4,
    'size_y': 4,
}

player = {
    'x': 1,
    'y': 1,
}

ghosts = [
    {
        'x': 3,
        'y': 0,
    },
    {
        'x': 3,
        'y': 3,
    }]

foods = [
    {
        'x': 0,
        'y': 0,
    },
    {
        'x': 1,
        'y': 0
    },
    {
        'x': 0,
        'y': 1,
    }]
    

playing = True

while playing:
    for y in range(map['size_y']):
        for x in range(map['size_x']):

            player_is_here = False
            if y == player['y'] and x == player['x']:
                player_is_here = True

            ghost_is_here = False
            for ghost in ghosts:
                if y == ghost['y'] and x == ghost['x']:
                    ghost_is_here = True

            food_is_here = False
            for food in foods:
                if y == food['y'] and x == food['x']:
                    food_is_here = True

            if player_is_here:
                print('P ',end='')
            elif ghost_is_here:
                print('G ',end='')
            elif food_is_here:
                print('F ',end='')
            else:
                print('- ',end='')
        print()

    
    
    # check win
    
    
    if len(foods) == 1 and player == food:
        print('You won!!!')
        break
    else:
        for food in foods:
            if player == food:
                foods.remove(food)
    
    if player == ghosts[1] or player == ghosts[0] :
        print('You lost!!!')
        break
        

    # bind button
    move = input('Your next move: ').upper()
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

    

    
    if 0 <= player['x'] + dx < map['size_x'] and \
        0 <= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy

    direct = [1, -1]
    fx = 0
    fy = 0
    move_rand = choice(direct)
    if move_rand == 1:
        fx = choice(direct)
    if move_rand == -1:
        fy = choice(direct)
    for food in foods:
        if ghosts[0] != ghosts[1] != food:
            if 0 <= ghosts[0]['x'] + fx < map['size_x'] and 0 <= ghosts[0]['y'] + fy < map['size_y']:
                ghosts[0]['x'] += fx
                ghosts[0]['y'] += fy
            if 0 <= ghosts[1]['x'] + fx < map['size_x'] and 0 <= ghosts[1]['y'] + fy < map['size_y']:
                ghosts[1]['x'] += fx
                ghosts[1]['y'] += fy
        
    
    

   

