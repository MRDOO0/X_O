def print_board(board):
    for row in board:
        print("".join(row))

def check_winner(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] != " - ":
            return True

    # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " - ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != " - ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " - ":
        return True

    return False

def play_game():
    while True:
        board = [
            [' - ', ' - ', ' - '],
            [' - ', ' - ', ' - '],
            [' - ', ' - ', ' - ']
        ]

        print("")
        print_board(board)

        i = 0
        while True:
            if i % 2 == 0:
                player = " X "
            else:
                player = " O "

            x = int(input("Your x (1-3): "))
            y = int(input("Your y (1-3): "))

            if x < 1 or x > 3 or y < 1 or y > 3:
                print("\033[91mInvalid input. Please try again.\033[0m")
                continue

            if board[y - 1][x - 1] != " - ":
                print("\033[91mPosition already occupied. Please try again.\033[0m")
                continue

            board[y - 1][x - 1] = player

            print_board(board)

            if check_winner(board):
                print("\033[91mPlayer", player, "wins!\033[0m")
                break

            if i == 8:
                print("It's a draw!")
                break

            i += 1

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


play_game()