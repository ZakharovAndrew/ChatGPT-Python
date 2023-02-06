import random



def draw_field():

    print('---------')

    print('|', end='')

    for i in range(3):

        for j in range(3):

            if field[i][j] == ' ':

                print(' ', end='')

            else:

                print(field[i][j], end='')

            if j != 2:

                print(' | ', end='')

        print()

        if i != 2:

            print('---------')

            print('|', end='')

    print('---------')





def get_state():

    state = ''

    for i in range(3):

        for j in range(3):

            state += field[i][j]

    return state



def check_win(state):

    winning_combinations = [

        '000XXX000',

        '111XXX111',

        '222XXX222',

        '000XXX111XXX222',

        '002XXX115XXX220', 

        '020XXX115XXX200',

        '022XXX111XXX220',

        '022XXX112XXX221',

    ]

    return state in winning_combinations





def make_step(x, y):

    if field[x][y] == ' ':

        field[x][y] = 'X'

    else:

        print('Bad move!')



def make_comp_step():

    for i in range(3):

        for j in range(3):

            if field[i][j] == ' ':

                field[i][j] = 'O'

                return None



def main():

    global field, turn 

    field = [[' ', ' ', ' '],

             [' ', ' ', ' '],

             [' ', ' ', ' ']]

    turn = 'X'

    while True:

        draw_field()

        if turn == 'X':

            x, y = map(int, input('Enter coords: ').split())

            make_step(x, y)

            turn = 'O'

        else:

            make_comp_step()

            turn = 'X'

        result = get_state()

        if check_win(result):

            draw_field()

            if turn == 'X':

                print('YOU WIN')

            else:

                print('COMP WIN')

            break



if __name__ == '__main__':

    main()