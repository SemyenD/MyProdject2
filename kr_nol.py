print("** Игра крестики-нолики **")
print()

def print_board(board):
    print()
    print("    | 0 | 1 | 2 |")
    print("--"*9)

    for i, row in enumerate(board):
        row_str = f"  {i} | {'  | '.join(row)}  |"
        print(row_str)
        print("--"*9)
    print()

def winner_var(board):
    for i in range (3):
        if board [i][0] == board [i][1] == board [i][2] !='':
            return board [i][0]
        if board[0][i] == board[1][i] == board[2][i] !='':
            return board[0][i]
        if board [0][0] == board [1][1] == board [2][2] !='':
            return board [0][0]
        if board[0][2] == board[1][i] == board[2][0] !='':
            return board[0][2]
    return None

def board_full(board):
    for row in board:
        if '' in row:
            return False
    return True

def play_game():
    board = [[""for i in range(3)]for i in range(3)]
    current_player = "X"
    win = None
    while not win and not board_full(board):
        print_board(board)
        print(f"Ходит {current_player}")
        x = int(input("Выберите строку:   "))
        y = int(input("Выберите колонку:  "))

        if 0 > x or x > 2 or 0 > y or y > 2:
            print()
            print("Координаты вне диапазона!")
            continue

        if board[x][y] !='':
            print("Эта клатка занята. Выберете клетку с другими координатами")
            continue


        board[x][y] = current_player
        win = winner_var(board)

        if current_player == "X":
            current_player = "0"
        else:
            current_player = "X"

            print_board(board)

        if win:
            print(f"Выиграл игрок {win}!")
        else:
            print("Ничья!")
play_game()