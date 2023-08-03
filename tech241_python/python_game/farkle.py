from os import system
from random import randint as roll_dice


def intro_screen():  # func: display intro to Game
    cs()
    print('Welcome to Farkle')
    input('Press <ENTER> to Start')


def get_players():  # func: how many players (2-5) and player names
    names = ['Player 1', 'Player 2']
    scores = {
        'Player 1': 0,
        'Player 2': 0
    }
    return names, scores


def play_game(names, scores):  # func: play game
    for player in names:
        cs()
        print('{}\'s turn'.format(player))
        print('')
        roll = roll_dice(1, 6)
        scores[player] += roll
        print('{} rolled a {}'.format(player, roll))
        input('Press <ENTER> to Continue')
    return scores


def get_winner(names, scores):  # func: who won and play again
    cs()
    print('{} scored {}, and {} scored {}'.format(names[0], scores[names[0]], names[1], scores[names[1]]))
    print('')
    if scores[names[0]] == scores[names[1]]:
        print('It was a Draw')
    elif scores[names[0]] >= scores[names[1]]:
        print('{} Won'.format(names[0]))
    elif scores[names[0]] <= scores[names[1]]:
        print('{} Won'.format(names[1]))
    print('')
    input('Press <ENTER> to Close')


def main():
    intro_screen()
    player_names, player_scores = get_players()
    player_scores = play_game(player_names, player_scores)
    get_winner(player_names, player_scores)


def cs():  # func: clear screen
    system("cls||clear")


if __name__ == '__main__':
    main()
