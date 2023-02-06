x1 = [" " for i in range(9)]



def grid():

    print (x1[0] + "|" + x1[1] + "|" + x1[2])

    print ("-+-+-")

    print (x1[3] + "|" + x1[4] + "|" + x1[5])

    print ("-+-+-")

    print (x1[6] + "|" + x1[7] + "|" + x1[8])



grid()



def move(letter, pos):

    x1[pos] = letter

    grid()



while True:

    move("X", int(input("Сделайте ход игрока X: ")))

    move("O", int(input("Сделайте ход игрока O: ")))

