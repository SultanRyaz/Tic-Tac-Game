def print_scheme():
    print(scheme[0], end=" ")
    print(scheme[1], end=" ")
    print(scheme[2])

    print(scheme[3], end=" ")
    print(scheme[4], end=" ")
    print(scheme[5])

    print(scheme[6], end=" ")
    print(scheme[7], end=" ")
    print(scheme[8])
scheme = [1, 2, 3, 4, 5, 6, 7, 8, 9]

end_game = False
player1 = input('Выберите, чем будет ходить игрок 1: ')
if player1 == "X":
    players = ["X", "0"]
if player1 == "0":
    players = ["0", "X"]
