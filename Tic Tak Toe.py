def board_print(board):
    row = [" {} | {} | {} ".format(board[0], board[1], board[2]),
           " {} | {} | {} ".format(board[3], board[4], board[5]),
           " {} | {} | {} ".format(board[6], board[7], board[8])]

    divider = "--- --- ---"

    for i in range(3):
        print(row[i])
        if i < 2:
            print(divider)


def check_winner(board, player):
    win_condition = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                     (0, 4, 8), (2, 4, 6)]             # diagonals

    for condition in win_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def draw(board):
    return all(cell != " " for cell in board)


def start():
    board = [" " for _ in range(9)]
    player = 'X'

    while True:
        board_print(board)
        number = 1 if player == 'X' else 2

        try:
            choice = int(input("Player {}, Enter Ur Move (1-9): ".format(number)))-1

            if choice < 0 or choice > 8:
                print("Invalid Move. Please enter a number between 1 and 9.\n")
                continue

            elif board[choice] != " ":
                print("Invalid Move, Cell Full. Try another Move.\n")
                continue

        except (ValueError, IndexError):
            print("Invalid Move. Enter a number between 1 and 9.\n")
            continue

        board[choice] = player

        if check_winner(board, player):
            print("You have WON player {}\n".format(number))
            board_print(board)
            break
        elif draw(board):
            print("Its a DRAW \n")
            board_print(board)
            break

        player = 'O' if player == 'X' else 'X'


start()
