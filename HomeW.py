import random

def main():
    print('SUPER FIGHT GAME!')
    player = None

    Player1 = {
        'name': 'Power man',
        'power': 15,
        'skill': 1.0,
        'health': 100,
    }

    Player2 = {
        'name': 'Healthy man',
        'power': 10,
        'skill': 1.0,
        'health': 150,
    }

    Player3 = {
        'name': 'Skill man',
        'power': 10,
        'skill': 2.0,
        'health': 100,
    }

    warrior = int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill'))
    if warrior == 1:
        player = Player1
    elif warrior == 2:
        player = Player2
    elif warrior == 3:
        player = Player3

    opponent_random = random.randint(1,3)

    if opponent_random == 1:
        opponent = Player1
    elif opponent_random == 2:
        opponent = Player2
    elif opponent_random == 3:
        opponent = Player3

    print('Your warrior: ', player['name'])
    print('Opponent: ', opponent['name'])

    win = False

    while True:
        print('Your player HP: ', player['health'])
        print('Opponent    HP: ', opponent['health'], '\n')

        kick = int(input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = '))
        block = int(input('Please select block: 1 - to head, 2 - to body, 3 - to foot = '))
        print('\n')
        opponent_kick = random.randint(1,3)
        opponent_block = random.randint(1,3)

        if kick != opponent_block:
            print('You hit an opponent!')
            opponent['health'] = opponent['health'] - (player['power'] * player['skill'])

        if block != opponent_kick:
            print('Opponent hit you :( ')
            player['health'] = player['health'] - (opponent['power'] * opponent['skill'])

        if player['health'] < 0:
            break

        if opponent['health'] < 0:
            win = True
            break

    if win:
        print('YOU WINNER!!!')
    else:
        print('GAME OVER.')


if __name__ == '__main__':
    main()
