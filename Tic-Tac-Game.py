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

def get_result():
    victory = ""

    for i in wins:
        if scheme[i[0]] == "X" and scheme[i[1]] == "X" and scheme[i[2]] == "X":
            victory = "X"
        elif scheme[i[0]] == "0" and scheme[i[1]] == "0" and scheme[i[2]] == "0":
            victory = "0"

    return victory

scheme = [1, 2, 3, 4, 5, 6, 7, 8, 9]
wins = [[3, 4, 5], [0, 1, 2], [6, 7, 8], [2, 4, 6], [0, 3, 6], [2, 5, 8], [1, 4, 7], [0, 4, 8]]

while end_game == False:

    print_scheme()

    if step == 0:
        symbol = players[step]
        move = int(input("Игрок 1, ваш ход: "))
        step = 1
    else:
        symbol = players[step]
        move = int(input("Игрок 2, ваш ход: "))
        step = 0

    move_scheme(move, symbol)
    victory = get_result()
    if victory != "":
        end_game = True
        victory = players.index(victory)
    else:
        end_game = False

print_scheme()
print("Победил игрок", victory+1)


def move_scheme(move, symbol):
    ind = scheme.index(move)
    scheme[ind] = symbol

