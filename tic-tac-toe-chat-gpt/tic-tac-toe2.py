def print_field():

    for i in range(3): 

        for j in range(3):

            print(field[i][j], end = ' ')

        print()



field = [['_' for i in range(3)] for j in range(3)]



while True:

    x = int(input("Введите позицию Х: "))

    y = int(input("Введите позицию Y: "))

    if field[x][y] == '_':

        field[x][y] = 'X'

    else:

        print("Это поле уже занято. Выберете другое")

        continue

    

    print_field()



    if (field[0][0] == 'X' and field[0][1] == 'X' and field[0][2] == 'X' or

        field[1][0] == 'X' and field[1][1] == 'X' and field[1][2] == 'X' or

        field[2][0] == 'X' and field[2][1] == 'X' and field[2][2] == 'X' or

        field[0][0] == 'X' and field[1][0] == 'X' and field[2][0] == 'X' or

        field[0][1] == 'X' and field[1][1] == 'X' and field[2][1] == 'X' or

        field[0][2] == 'X' and field[1][2] == 'X' and field[2][2] == 'X' or

        field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X' or

        field[2][0] == 'X' and field[1][1] == 'X' and field[0][2] == 'X'):

        print("Вы выиграли")

        break

    elif (field[0][0] != '_' and field[0][1] != '_' and field[0][2] != '_' and

          field[1][0] != '_' and field[1][1] != '_' and field[1][2] != '_' and

          field[2][0] != '_' and field[2][1] != '_' and field[2][2] != '_'):

        print("Ничья")

        break

    

    x = int(input("Введите позицию О: "))

    y = int(input("Введите позицию Y: "))

    if field[x][y] == '_':

        field[x][y] = 'O'

    else:

        print("Это поле уже занято. Выберете другое")

        continue

    

    print_field()

    

    if (field[0][0] == 'O' and field[0][1] == 'O' and field[0][2] == 'O' or

        field[1][0] == 'O' and field[1][1] == 'O' and field[1][2] == 'O' or

        field[2][0] == 'O' and field[2][1] == 'O' and field[2][2] == 'O' or

        field[0][0] == 'O' and field[1][0] == 'O' and field[2][0] == 'O' or

        field[0][1] == 'O' and field[1][1] == 'O' and field[2][1] == 'O' or

        field[0][2] == 'O' and field[1][2] == 'O' and field[2][2] == 'O' or

        field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O'):

        print("Выиграл 0")

        break